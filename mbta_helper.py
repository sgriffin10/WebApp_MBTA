'''Belongs to Brach 1'''
# A little bit of scaffolding if you want to use it
from api_credentials import *
import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = 'YOUR API KEY: 	fCqG7G2TwuZI9OpIwFHbqMZThj3EZoin'

#to call MBTA API KEY, TRY THE FOLLOWING: 

f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)
    print(response_data["results"][0]["locations"][0]['postalCode'])



def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    dict_response_data = response_data["results"][0]["locations"][0]['latLng']
    print(dict_response_data)
    # latlong_s = set(['lat','long'])
    # print(latlong_s)
    # print(zip(latlong_s, dict_response_data))
    # for pair in zip(latlong_s, dict_response_data):
    #     print(pair)




def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """

    
    pass


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    pass


def main():
    """
    You can call the functions here
    """
    # #get_json
    # url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    # print(get_json(url))
    # #get_lat_long
    place_name = 'Beijing'
    get_lat_long(place_name)


if __name__ == '__main__':
    main()
