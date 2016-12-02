import json
import codecs
import os


def load_data(filepath):
    if os.path.exists(filepath):
        file_handler = codecs.open(filepath, 'r', 'utf-8')
        return json.load(file_handler)
    else:
        raise SystemExit('Wrong file path')


def get_biggest_bar(bars_list):
    if not bars_list:
        SystemExit('Empty list of bars')
    max_seats = bars_list[1]['SeatsCount']
    for bar in bars_list:
        if bar['SeatsCount'] > max_seats:
            max_seats = bar['SeatsCount']
            name_address = bar['Name'] + ' located at ' + bar['Address']
    return name_address


def get_smallest_bar(bars_list):
    if not bars_list:
        SystemExit('Empty list of bars')
    min_seats = bars_list[1]['SeatsCount']
    for bar in bars_list:
        if bar['SeatsCount'] <= min_seats:
            min_seats = bar['SeatsCount']
            name_address = bar['Name'] + ' located at ' + bar['Address']
    return name_address


def get_closest_bar(bars_list, user_longitude, user_latitude):
    minimal_distance = abs(float(bars_list[1]['Latitude_WGS84']) -
                           user_latitude) + \
                           abs(float(bars_list[1]['Longitude_WGS84']) -
                               user_longitude)
    for bar in bars_list:
        bar_latitude = float(bar['Latitude_WGS84'])
        bar_longitude = float(bar['Longitude_WGS84'])
        distance_estimate = abs(bar_latitude - user_latitude) + \
            abs(bar_longitude - user_longitude)
        if distance_estimate < minimal_distance:
            minimal_distance = distance_estimate
            name_address = bar['Name'] + ' located at ' + bar['Address']
    return name_address

if __name__ == '__main__':
    json_filepath = input('Enter filepath' + '\n')
    bars_list = load_data(json_filepath)
    try:
        user_longitude = float(input('Enter your current longitude\n'))
    except ValueError:
        raise SystemExit('Longitude must be a number')
    try:
        user_latitude = float(input('Enter your current latitude\n'))
    except ValueError:
        raise SystemExit('Latutude must be a number')

    print('The biggest bar: {}'.format(get_biggest_bar(bars_list)))
    print('The smallest bar: {}'.format(get_smallest_bar(bars_list)))
    print('The closest bar: {}'.format(get_closest_bar(bars_list,
                                                       user_longitude,
                                                       user_latitude)))

