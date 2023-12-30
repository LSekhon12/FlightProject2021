"""CSC108H5S: Functions for Assignment 3 - OpenFlights.

Instructions (READ THIS FIRST!)
===============================

Make sure that all the assignment files (flight_program.py, flight_reader.py,
etc.) are in the same directory as this file.

This file contains the starter code for reading data from files.

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Mario Badr, Tom Fairgrieve, Amanjit Kainth, Kaveh Mahdaviani,
Sadia Sharmin, Jarrod Servilla, and Joseph Jay Williams
"""

from typing import TextIO, List

from flight_constants import AirportsDict, RoutesDict, FlightDict, \
     OPENFLIGHTS_NULL_VALUE

import flight_example_data


################################################################################
# Part 1 - Reading the data
################################################################################

def read_airports(airports_source: TextIO) -> AirportsDict:
    """Return a dictionary containing the information in airports_source.
    The dictionary maps IATA airport codes to a sub-dictionary containing
    information about that airport.

    Any entries that have a null IATA code in airports_source should NOT be
    included in this dictionary.
    
    The sub-dictionaries containing information about each airport have str keys
    that identify the information category (these keys come from the categories
    in the header line in airports_source), and the value is the respective
    data for that airport, for that category, as given in airports_source.

    Precondition:
    - Every IATA airport code in the data is unique
    - The data in airports_source is formatted correctly
        
    >>> example_airport_file = flight_example_data.create_airport_file()
    >>> airports_res = read_airports(example_airport_file)
    >>> airports_res['AA1']['Airport ID'], airports_res['AA1']['Name']
    ('1', 'Apt1')
    >>> airports_res['AA4']['Airport ID'], airports_res['AA4']['Name']
    ('4', 'Apt4')
    >>> len(airports_res)
    4
    >>> airports_res == flight_example_data.create_example_airports()
    True
    """

    airport_dict = {}
    categories = airports_source.readline().strip().split(",")
    iata_index = categories.index("IATA")
    line = airports_source.readline()
    while line is not None and line != '':
        lst = line.strip().split(",")
        if lst[iata_index] == OPENFLIGHTS_NULL_VALUE:
            line = airports_source.readline()
            continue
        cur = {}
        for cat_idx in range(len(categories)):
            cat = categories[cat_idx]
            cur[cat] = lst[cat_idx]
        airport_dict[lst[iata_index]] = cur
        line = airports_source.readline()
    return airport_dict


def read_routes(routes_source: TextIO, airports: AirportsDict) -> RoutesDict:
    """Return the flight routes from routes_source, including only the ones
    that have an entry in airports. That is, any route that has a source
    or destination airport code which does not appear in the given AirportDict
    should not be included in the resulting RouteDict.
    
    If there are multiple routes from a route source to a destination
    (on different airlines for example), include the destination only once.

    Precondition:
        - The data in routes_source is formatted correctly

    >>> routes_src = flight_example_data.create_route_file()
    >>> example_airports = flight_example_data.create_example_airports()
    >>> actual = read_routes(routes_src, example_airports)
    >>> actual == flight_example_data.create_example_routes()
    True
    """

    routes_dict = {}
    categories = routes_source.readline().strip().split(",")
    src_index = categories.index("Source airport")
    dst_index = categories.index("Destination airport")
    line = routes_source.readline()
    while line is not None and line != '':
        lst = line.strip().split(",")
        src = lst[src_index]
        dst = lst[dst_index]
        if airports.get(src) is None or airports.get(dst) is None:
            line = routes_source.readline()
            continue
        if routes_dict.get(src) is None:
            routes_dict[src] = [dst]
        else:
            routes_dict[src].append(dst)
        line = routes_source.readline()
    return routes_dict



def read_flights(flights_source: TextIO, routes: RoutesDict) -> \
    List[FlightDict]:
    """Return the flight data from flights_source, including only the ones
    that have an entry in routes. That is, any flight that has a source
    and destination airport code which does not appear as a valid route in
    the given RouteDict should NOT be included in the resulting FlightList.

    Precondition:
        - The data in flights_source is formatted correctly
        
    >>> flight_src = flight_example_data.create_flight_file()
    >>> routes_example = flight_example_data.create_example_routes()
    >>> actual = read_flights(flight_src, routes_example)
    >>> actual == flight_example_data.create_example_flights()
    True
    """
   
    flights = []
    categories = flights_source.readline().strip().split(",")
    src_index = categories.index("Source airport")
    dst_index = categories.index("Destination airport")
    float_indexes = [categories.index("Departure time"), \
        categories.index("Duration")]
    line = flights_source.readline()
    while line is not None and line != '':
        lst = line.strip().split(",")
        src = lst[src_index]
        dst = lst[dst_index]
        # source not included
        if routes.get(src) is None:
            line = flights_source.readline()
            continue
        destination_exists = False
        for dest in routes.get(src):
            destination_exists |= (dest == dst)
        # source exists but not destination
        if not destination_exists:
            line = flights_source.readline()
            continue
        # both source and destination exist. Hence, add that line.
        cur = {}
        for i in range(len(categories)):
            if i in float_indexes:
                cur[categories[i]] = float(lst[i])
            else:
                cur[categories[i]] = lst[i]
        flights.append(cur)
        line = flights_source.readline()
    return flights


if __name__ == "__main__":

    # Uncomment to check the correctness of the doctest examples
    import doctest
    #doctest.testmod()

    # Uncomment the lines below to open the files and call your functions above
    airport_file = open('data/airports.csv', encoding='utf8')
    airport_data = read_airports(airport_file)
    # print(airport_data)
    airport_file.close()
    
    routes_file = open('data/routes.csv', encoding='utf8')
    route_data = read_routes(routes_file, airport_data)
    routes_file.close()

    flights_file = open('data/flights.csv', encoding='utf8')
    flight_data = read_flights(flights_file, route_data)
    flights_file.close()

    # Some basic tests to see that you read the files right
    assert len(airport_data) == 2263
    assert len(route_data) == 1556
    assert len(flight_data) == 8964

