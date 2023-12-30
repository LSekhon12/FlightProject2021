from typing import TextIO, List

from flight_constants import AirportsDict, RoutesDict, FlightDict, \
     OPENFLIGHTS_NULL_VALUE
from typing import Dict, List, Union

import flight_example_data
from flight_reader import read_airports

example_airport_file = flight_example_data.create_airport_file()
mat = []
for line in example_airport_file.readlines():
    print(line)
    lst = line.split(',')
    print(lst)
    mat.append(lst)
result: AirportsDict = {}
for j in range(len(mat[0])):
    cur: Dict[str, str] = {}
    for i in range(1, len(mat)):
    # source that's they key for our dict
        if j == (len(mat[0]) - 1):
            # cur.setdefault()
            result[mat[i][j]] = cur
        else:
            cur[mat[0][j]] = mat[i][j]
    # prop = mat[0][i]
    # result[mat[0][13]] = Dict
print(result)

airports_res = read_airports(example_airport_file)
airports_res['AA1']['Airport ID'], airports_res['AA1']['Name']
    # ('1', 'Apt1')
airports_res['AA4']['Airport ID'], airports_res['AA4']['Name']
    # ('4', 'Apt4')
len(airports_res)
    # 4
airports_res == flight_example_data.create_example_airports()
    # True

