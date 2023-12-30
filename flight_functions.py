"""CSC108H5S: Functions for Assignment 3 - Airports and Routes.

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Mario Badr, Tom Fairgrieve, Amanjit Kainth, Kaveh Mahdaviani,
Jarrod Servilla, Sadia Sharmin, and Joseph Jay Williams
"""
from typing import Dict, List, Optional, Tuple, Union

from flight_constants import AirportsDict, RoutesDict, FlightDict, \
     OPENFLIGHTS_NULL_VALUE

import flight_example_data


################################################################################
# Part 2 - Querying the data
################################################################################

def get_airport_info(airports: AirportsDict, iata: str, info: str) -> str:
    """Return the airport information for airport with IATA code iata
    associated with info.

    Precondition(s):
    - iata is a valid code that exists in the airports dictionary
    - info is a valid key that exists in each airport sub-dictionary

    >>> airport_example_data = flight_example_data.create_example_airports()
    >>> get_airport_info(airport_example_data, 'AA1', 'Name')
    'Apt1'
    >>> get_airport_info(airport_example_data, 'AA4', 'IATA')
    'AA4'
    """
    return airports[iata][info]


def is_direct_flight(iata_src: str, iata_dst: str, routes: RoutesDict) -> bool:
    """Return whether there is a direct flight from the iata_src airport to
    the iata_dst airport in the routes dictionary. iata_src may not
    be a key in the routes dictionary.

    >>> routes_example_data = flight_example_data.create_example_routes()
    >>> is_direct_flight('AA1', 'AA2', routes_example_data)
    True
    >>> is_direct_flight('AA2', 'AA1', routes_example_data)
    False
    """
    for dest in routes[iata_src]:
        if dest == iata_dst:
            return True
    return False


def is_valid_flight_sequence(iata_list: List[str], routes: RoutesDict) -> bool:
    """Return whether there are flights from iata_list[i] to iata_list[i + 1]
    for all valid values of i. IATA entries may not appear anywhere in routes.

    >>> routes_example_data = flight_example_data.create_example_routes()
    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2'], routes_example_data)
    True
    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2', 'AA1', 'AA2'], \
    routes_example_data)
    False
    """
    for i in range(len(iata_list) - 1):
        src = iata_list[i]
        dst = iata_list[i + 1]
        if not is_direct_flight(src, dst, routes):
            return False
    return True


def get_remaining_flights_today(flights: List[FlightDict], \
                                curr_time: float) -> List[FlightDict]:
    """The first parameter represents a list of information about 
    all available flights. 
    The second parameter represents a specific time (a float from 0.0 
    to 24.0 representing 
    the 24-hour clock). Return a list of all flights that are remaining today 
    (their departure time should be greater than or equal to 
    the given current time).

    Note that each flight information in the resulting list should be in a 
    FlightDict format as previously described in this handout.

    You may assume the given input (the flight information and 
    the current time) will be valid.
    """
    rem_flights = []
    for flight in flights:
        if curr_time < flight['Departure time']:
            rem_flights.append(flight)
    return rem_flights


################################################################################
# Part 3 - Implementing useful algorithms
################################################################################

def get_best_flight(iata_src: str, iata_dst: str, flights: List[FlightDict], \
                    curr_time: float = 0.0) -> Optional[FlightDict]:
    """
    Return a flight in FlightList flights that is departing from
    iata_src and arriving to iata_dst. If there are multiple such flights,
    return the one that will get to the destination the soonest based on the
    given current time (curr_time), the flight's departure time and
    the flight's duration.

    If a current time is not provided, give the best flight starting from the
    beginning of the day (beginning of day is when time = 0.0).
    
    If there is no flight from the given source to given destination,
    return None.
    """
    shortest_time_so_far = float('inf')
    best_flight = None
    
    for flight in flights:
        dst = flight['Destination airport']
        src = flight['Source airport']
        if dst == iata_dst and src == iata_src:
            travel_time = flight['Duration']
            waiting_time = float(flight['Departure time']) - curr_time
            if waiting_time < 0:
                waiting_time += 24
            travel_time += waiting_time
            if shortest_time_so_far > travel_time:
                shortest_time_so_far = travel_time
                best_flight = flight
        
    return best_flight


def find_reachable_destinations(iata_src: str, n: int, routes: RoutesDict) \
    -> List[str]:
    """Return the list of IATA airport codes that are reachable from iata_src by
    taking at most n direct flights.

    The list should not contain an IATA airport code more than once. The airport
    codes in the list should appear in increasing alphabetical/numerical order
    (use the list.sort method on a list of strings to achieve this).

    Preconditions:
        - n >= 1
        - (iata_src in routes) is True

    >>> routes_example_data = flight_example_data.create_example_routes()
    >>> find_reachable_destinations('AA1', 1, routes_example_data)
    ['AA2', 'AA4']
    >>> find_reachable_destinations('AA1', 2, routes_example_data)
    ['AA1', 'AA2', 'AA3', 'AA4']
    """
    if n == 0:
        return [iata_src]
    ret = []
    for dest in routes[iata_src]:
        cur = find_reachable_destinations(dest, n - 1, routes)
        ret += cur
        ret += [dest]
    return sorted(list(dict.fromkeys(ret)))
        

def calculate_trip_time(path: List[str], flights: List[FlightDict]) -> float:
    """Return a float representing the arrival time after travelling from
    the source airport to a destination airport, through the provided path
    of flights.

    The start time of the trip is the beginning of the day (i.e. time is 0.0).

    Precondition:
    - The source airport appears at path[0]
    - The destination airport appears at path[-1]
    - The path given is a valid path of flights (i.e. there exists a direct
    flight between each adjacent flight in the path list)

    >>> flights_example_data = flight_example_data.create_example_flights()
    >>> calculate_trip_time(["AA1", "AA2"], flights_example_data)
    2.0
    >>> calculate_trip_time(["AA1"], flights_example_data)
    0.0
    >>> calculate_trip_time(["AA4", "AA1", "AA2"], flights_example_data)
    14.0
    >>> calculate_trip_time(["AA1", "AA2", "AA3"], flights_example_data)
    7.5
    >>> calculate_trip_time(["AA3", "AA4", "AA1"], flights_example_data)
    29.0
    22.5 -> 2.0
    """
    nb_days = 0
    last_arrival_time = 0.0
    
    for i in range(len(path) - 1):
        src = path[i]
        dst = path[i + 1]
        best_flight = get_best_flight(src, dst, flights, last_arrival_time)
        cur_arrival_time = float(best_flight['Duration'])
        cur_arrival_time += float(best_flight['Departure time'])
        if cur_arrival_time < last_arrival_time:
            nb_days += 1
        last_arrival_time = cur_arrival_time
    return nb_days * 24 + last_arrival_time

if __name__ == "__main__":
    # Uncomment to check the correctness of the doctest examples
    import doctest
    #doctest.testmod()

if __name__ == "__main__":
    # Uncomment to check the correctness of the doctest examples
    import doctest
    #doctest.testmod()

    # Uncomment to check a few correctness tests that use our real data files
    # You can add more of your own tests
    # Note that the following won't work if your part 1 is incomplete/incorrect
    from flight_reader import read_airports, read_routes, read_flights
    
    airport_file = open('data/airports.csv', encoding='utf8')
    airport_data = read_airports(airport_file)
    airport_file.close()

    assert get_airport_info(airport_data, "YYZ", "Name") == \
          "Lester B. Pearson International Airport"
    assert get_airport_info(airport_data, "YYZ", "City") == "Toronto"
    
    routes_file = open('data/routes.csv', encoding='utf8')
    route_data = read_routes(routes_file, airport_data)
    routes_file.close()

    assert is_direct_flight("PUJ", "LED", route_data) # check if True
    
    flights_file = open('data/flights.csv', encoding='utf8')
    flight_data = read_flights(flights_file, route_data)
    flights_file.close()
    # print(calculate_trip_time(["LIM", "AYP"], flight_data))
    # print(find_reachable_destinations("LIM", 1,route_data))
    assert calculate_trip_time(["LIM", "AYP"], flight_data) == 22.5 
    
    

