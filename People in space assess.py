import requests
import json
def filter_astronauts_by_nationality(iss_response, nationality):
    filtered_astronauts = []

    if 'people' in iss_response:
        astronauts = iss_response['people']

        for astronaut in astronauts:
            if 'nationality' in astronaut and astronaut['nationality'] == nationality:
                filtered_astronauts.append(astronaut)

            return filtered_astronauts
        
service_url = ('http://api.open-notify.org/astros.json')

try:
    response = requests.get(service_url)
    response.raise_for_status()

    iss_response = response.json()
    number = iss_response.get('number')

    
    if number is not None:
        people = iss_response.get('people')
        print(f'Number :{number}') 
            
        if people is not None:
            print(f'People : {people}')
        else:
            print('Number of people not found')
    else:
        print('People not found')

except requests.exceptions.RequestException as e:
    print(f"Error:{e}")

