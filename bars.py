import json
import codecs
import os


def load_data(file_path):
    if os.path.exists(file_path):
        with codecs.open(file_path, 'r', 'utf-8') as file_handler:
            return json.load(file_handler)
    else:
        raise SystemExit('Wrong file path')


def get_biggest_bar(bars_list):
    return [max(bars_list, key=lambda x:
            x['SeatsCount'])[x] for x in ['Name', 'Address']]


def get_smallest_bar(bars_list):
    return [min(bars_list, key=lambda x:
            x['SeatsCount'])[x] for x in ['Name', 'Address']]


def get_closest_bar(bars_list, usr_longitude, usr_latitude):
    return [min(bars_list, key=lambda x:
            abs(float(x['Latitude_WGS84']) - usr_latitude) +
            abs(float(x['Longitude_WGS84']) - usr_longitude))[x]
            for x in ['Name', 'Address']]


def get_user_coordinate(coordinate_name):
    try:
        return float(input('Enter your'
                           ' current {}\n'.format(coordinate_name.lower())))
    except ValueError:
        raise SystemExit('{} must be a number'.format(coordinate_name))


if __name__ == '__main__':
    list_of_bars = load_data(input('Enter file path\n'))
    user_longitude = get_user_coordinate('Longitude')
    user_latitude = get_user_coordinate('Latitude')
    print('The biggest bar is {},'
          ' located at {}'.format(*get_biggest_bar(list_of_bars)))
    print('The smallest bar is {},'
          ' located at {}'.format(*get_smallest_bar(list_of_bars)))
    print('The closest bar is {},'
          ' located at {}'.format(*get_closest_bar(list_of_bars,
                                                   user_longitude,
                                                   user_latitude)))
