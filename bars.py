import json
import codecs
import os
from operator import itemgetter


def load_data(file_path):
    if os.path.exists(file_path):
        with codecs.open(file_path, 'r', 'utf-8') as file_handler:
            return json.load(file_handler)
    else:
        raise SystemExit('Wrong file path')


def get_biggest_bar(bars_list):
    return [max(bars_list,
                key=itemgetter('SeatsCount'))[x] for x in ['Name', 'Address']]


def get_smallest_bar(bars_list):
    return [min(bars_list,
                key=itemgetter('SeatsCount'))[x] for x in ['Name', 'Address']]


def get_closest_bar(bars_list, usr_longitude, usr_latitude):
    estimated_distances = []
    for bar in bars_list:
        estimated_distances.append(abs(float(bar['Latitude_WGS84']) -
                                       usr_latitude) +
                                   abs(float(bar['Longitude_WGS84']) -
                                       usr_longitude))
    return [bars_list[estimated_distances.index(min(estimated_distances))][x]
            for x in ['Name', 'Address']]

if __name__ == '__main__':
    list_of_bars = load_data(input('Enter file path' + '\n'))
    try:
        user_longitude = float(input('Enter your current longitude\n'))
    except ValueError:
        raise SystemExit('Longitude must be a number')
    try:
        user_latitude = float(input('Enter your current latitude\n'))
    except ValueError:
        raise SystemExit('Latitude must be a number')
    print('The biggest bar is {},'
          ' located at {}'.format(*get_biggest_bar(list_of_bars)))
    print('The smallest bar is {},'
          ' located at {}'.format(*get_smallest_bar(list_of_bars)))
    print('The closest bar is {},'
          ' located at {}'.format(*get_closest_bar(list_of_bars,
                                                   user_longitude,
                                                   user_latitude)))
