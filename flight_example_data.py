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
# Note about "from io import StringIO":
# We can use StringIO to pretend that a string is the contents of a file.

from io import StringIO

from typing import List

from flight_constants import AirportsDict, RoutesDict, FlightDict


def create_airport_file() -> StringIO:
    """Return a "dummy file" with airport data to use for docstring examples.

    WARNING: Do NOT change this function.
    """

    s = '''Airport ID,Name,City,Country,IATA,ICAO,Latitude,Longitude,Altitude,Timezone,DST,Tz,Type,Source
    1,Apt1,Cty1,Cntry1,AA1,AAA1,-1,1,1,1,1,D1,Typ1,Src1
    2,Apt2,Cty2,Cntry2,AA2,AAA2,-2,2,2,2,2,D2,Type2,Src2
    3,Apt3,Cty3,Cntry3,AA3,AAA3,-3,3,3,3,3,D3,Type3,Src3
    4,Apt4,Cty4,Cntry4,AA4,AAA4,-4,4,4,4,4,D4,Type4,Src4
    5,Apt5,Cty5,Cntry5,\\N,AAA5,-5,5,5,5,5,D5,Type5,Src5'''

    return StringIO(s)


def create_example_airports() -> AirportsDict:
    """Return the AirportDict that should be produced when reading the data
    from create_airport_file.

    WARNING: Do NOT change this function.
    """

    return {
    "AA1": {
        "Airport ID": "1",
        "Name": "Apt1",
        "City": "Cty1",
        "Country": "Cntry1",
        "IATA": "AA1",
        "ICAO": "AAA1",
        "Latitude": "-1",
        "Longitude": "1",
        "Altitude": "1",
        "Timezone": "1",
        "DST": "1",
        "Tz": "D1",
        "Type": "Typ1",
        "Source": "Src1",
    },
    "AA2": {
        "Airport ID": "2",
        "Name": "Apt2",
        "City": "Cty2",
        "Country": "Cntry2",
        "IATA": "AA2",
        "ICAO": "AAA2",
        "Latitude": "-2",
        "Longitude": "2",
        "Altitude": "2",
        "Timezone": "2",
        "DST": "2",
        "Tz": "D2",
        "Type": "Type2",
        "Source": "Src2",
    },
    "AA3": {
        "Airport ID": "3",
        "Name": "Apt3",
        "City": "Cty3",
        "Country": "Cntry3",
        "IATA": "AA3",
        "ICAO": "AAA3",
        "Latitude": "-3",
        "Longitude": "3",
        "Altitude": "3",
        "Timezone": "3",
        "DST": "3",
        "Tz": "D3",
        "Type": "Type3",
        "Source": "Src3",
    },
    "AA4": {
        "Airport ID": "4",
        "Name": "Apt4",
        "City": "Cty4",
        "Country": "Cntry4",
        "IATA": "AA4",
        "ICAO": "AAA4",
        "Latitude": "-4",
        "Longitude": "4",
        "Altitude": "4",
        "Timezone": "4",
        "DST": "4",
        "Tz": "D4",
        "Type": "Type4",
        "Source": "Src4",
    },
    }


# Routes between the tests airports. A StringIO object can use this as an
# input source for purposes of testing.
# The graph is: 1->2, 2->3, 3->4, 4->1, 1->4, and 3->1
def create_route_file() -> StringIO:
    """Return a "dummy file" with route data to use for docstring examples.

    WARNING: Do NOT change this function.
    """
    
    s = """Airline,Airline ID,Source airport,Source airport ID,Destination airport,Destination airport ID,Codeshare,Stops,Equipment
A1,1111,AA1,1,AA2,2,,0,EQ1
A2,2222,AA2,2,AA3,3,,0,EQ1
A3,3333,AA3,3,AA4,4,,0,EQ1
A4,4444,AA4,4,AA1,1,,0,EQ1
A1,1111,AA1,1,AA4,4,,0,EQ1
A3,3333,AA3,3,AA1,1,,0,EQ1
"""

    return StringIO(s)


# The flight routes for the routes above
def create_example_routes() -> RoutesDict:
    """Return the RouteDict that should be produced when reading the data
    from create_route_file and including only the airports from
    create_example_airports.

    WARNING: Do NOT change this function.
    """

    return {
    "AA1": ["AA2", "AA4"],
    "AA2": ["AA3"],
    "AA3": ["AA4", "AA1"],
    "AA4": ["AA1"],
    }


def create_flight_file() -> StringIO:
    """Return a "dummy file" with flight data to use for docstring examples.

    WARNING: Do NOT change this function.
    """

    s = """Flight ID,Source airport,Destination airport,Departure time,Duration
1,AA1,AA2,0.00,2.00
2,AA2,AA3,4.00,3.50
3,AA3,AA4,7.00,2.00
4,AA4,AA1,2.00,3.00
5,AA1,AA4,0.00,2.00
6,AA1,AA2,12.00,2.00
7,AA5,AA1,13.50,1.00
"""

    return StringIO(s)


def create_example_flights() -> List[FlightDict]:
    """Return the RouteDict that should be produced when reading the data
    from create_route_file and including only the airports from
    create_example_airports.

    WARNING: Do NOT change this function.
    """

    return [
        {'Flight ID': '1',
         'Source airport': 'AA1',
         'Destination airport': 'AA2',
         'Departure time': 0.00,
         'Duration': 2.00},
        {'Flight ID': '2',
         'Source airport': 'AA2',
         'Destination airport': 'AA3',
         'Departure time': 4.00,
         'Duration': 3.50},
        {'Flight ID': '3',
         'Source airport': 'AA3',
         'Destination airport': 'AA4',
         'Departure time': 7.00,
         'Duration': 2.00},
        {'Flight ID': '4',
         'Source airport': 'AA4',
         'Destination airport': 'AA1',
         'Departure time': 2.00,
         'Duration': 3.00},
        {'Flight ID': '5',
         'Source airport': 'AA1',
         'Destination airport': 'AA4',
         'Departure time': 0.00,
         'Duration': 2.00},
        {'Flight ID': '6',
         'Source airport': 'AA1',
         'Destination airport': 'AA2',
         'Departure time': 12.00,
         'Duration': 2.00}
        ]

