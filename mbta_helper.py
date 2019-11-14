'''Belongs to Branch 1'''
# A little bit of scaffolding if you want to use it
from api_credentials import *
import urllib.request
import json
from pprint import pprint

from flask import Flask, escape, url_for

app = Flask(__name__)

# MAPQUEST_API_KEY = 'YOUR API KEY: 	fCqG7G2TwuZI9OpIwFHbqMZThj3EZoin'

#to call MBTA API KEY, TRY THE FOLLOWING: 

# f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return response_data
    


# @app.route("/hello/")
@app.route("/homepage/<place_name>")
def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place = place_name.replace(' ', '%20')
    url = '{}?key={}&location={}'.format(MAPQUEST_BASE_URL, MAPQUEST_API_KEY,place)
    # print(url)
    place_json = get_json(url)
    lat = place_json["results"][0]["locations"][0]["latLng"]["lat"]
    lng = place_json["results"][0]["locations"][0]["latLng"]["lng"]
    print(f'({lat}, {lng})')
    return lat, lng

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
    return get_nearest_station(*get_lat_long(place_name))


def main():
    """
    You can call the functions here
    """
    #get_json
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    # print(get_json(url))
    #get_lat_long
    place_name = 'Babson College'
    get_lat_long(place_name)


if __name__ == '__main__':
    main()
