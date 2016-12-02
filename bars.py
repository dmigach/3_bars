
# coding: utf-8

# In[2]:

import json
import codecs


def load_data(filepath):
    file = codecs.open(filepath, 'r', 'utf-8')
    return json.load(file)


def get_biggest_bar(data):
    maxSeats = 0
    nameAddress = ''
    for bar in data:
        if bar['SeatsCount'] > maxSeats:
            maxSeats = bar['SeatsCount']
            nameAddress = bar['Name'] + ' located at ' + bar['Address']
    return (nameAddress)


def get_smallest_bar(data):
    minSeats = data[1]['SeatsCount']
    nameAddress = ''
    for bar in data:
        if bar['SeatsCount'] <= minSeats:
            minSeats = bar['SeatsCount']
            nameAddress = bar['Name'] + ' located at ' + bar['Address']
    return (nameAddress)


def get_closest_bar(data, longitude, latitude):
    minimalDistance = abs(float(data[1]['Latitude_WGS84']) - latitude) +                       abs(float(data[1]['Longitude_WGS84']) - longitude)
    nameAddress = ''
    for bar in data:
        barLatitude = float(bar['Latitude_WGS84'])
        barLongitude = float(bar['Longitude_WGS84'])
        distance = abs(barLatitude - latitude) + abs(barLongitude - longitude)
        if distance < minimalDistance:
            minimalDistance = distance
            nameAddress = bar['Name'] + ' located at ' + bar['Address']
    return (nameAddress)

if __name__ == '__main__':
    data = load_data(input('Enter filepath' + '\n'))
    print('The biggest bar: {}'.format(get_biggest_bar(data)))
    print('The smallest bar: {}'.format(get_smallest_bar(data)))
    print('The closest bar: {}'.format(
        get_closest_bar(data, float(input('Enter your current longitude\n')),
                        float(input('Enter your current latitude\n')))))


# In[144]:

data = load_data(input('Введите путь к файлу' + '\n'))


# In[135]:

decode('Windows-1252').encode('utf-8')

