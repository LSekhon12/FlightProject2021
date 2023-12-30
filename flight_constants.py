"""CSC108H1S: Functions for Assignment 3 - Airports and Routes.

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
from typing import Dict, List, Union

################################################################################
# Constants
################################################################################
OPENFLIGHTS_NULL_VALUE = '\\N'

################################################################################
# An AirportsDict is a dictionary that maps IATA airport codes to a dictionary
# that contains more information about the airport (e.g., name, country, etc.)
# with key = the category of information, and value = the information itself
################################################################################
AirportsDict = Dict[str, Dict[str, str]]

################################################################################
# A RouteDict is a dictionary that maps IATA airport codes to a list of
# destinations (representated as IATA codes) that are reachable from that
# airport.
################################################################################
RoutesDict = Dict[str, List[str]]

################################################################################
# A FlightDict is a dictionary of flight data (flight ID, source airport,
# dest airport, departure time, duration) for ONE flight. The flight ID,
# source airport, dest airport are all strings, and the departure time
# and duration are floats (the time can be from 0.0 to 24.0 representing
# a 24-hour clock).
################################################################################
FlightDict = Dict[str, Union[str, float]]
