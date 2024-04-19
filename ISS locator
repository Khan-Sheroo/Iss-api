import requests
import json

service_url = 'http://api.open-notify.org/iss-now.json'

try:
    response = requests.get(service_url)
    response.raise_for_status()
    ISS_location_response = response.json()

    if 'timestamp' in ISS_location_response and 'iss_position' in ISS_location_response and 'latitude' in ISS_location_response['iss_position'] and 'longitude' in ISS_location_response['iss_position']:
        timestamp = ISS_location_response['timestamp']
        latitude = ISS_location_response['iss_position']['latitude']
        longitude = ISS_location_response['iss_position']['longitude']
        print(f"timestamp: {timestamp}")
        print(f"ISS postion - latitude: {latitude}, longitude: {longitude}")
    else:
        print("Data not found, Check API for changes")


except requests.exceptions.RequestException as e:
    print(f"Error:{e}")

