import numpy as np
import pandas as pd
from tqdm.auto import tqdm
# from geopy.geocoders import Nominatim
from opencage.geocoder import OpenCageGeocode

#geocoder key
key = 'f1f7399fd125406faee7765413cca016'

#defining our function to get the geolocator per city
def get_location(address, geolocator):
    try:
        location = geolocator.geocode(address, no_annotations='1')
        return (location.latitude, location.longitude)
    except:
        return (None, None)        

#setting up our dataframe
def add_csv_coordinates(file_path, output_path):
    csv = pd.read_csv(file_path)
    df = pd.DataFrame(csv)

    #Instantiating a new Nominatim client
    # app = Nominatim(user_agent='road_trip')
    geocoder = OpenCageGeocode(key)

    #Getting our latitude and longitude
    tqdm.pandas()
    df['latitude'], df['longitude'] = zip(*df['Route Finish'].progress_apply(lambda x: get_location(x, geocoder)))

    #updating and returning the csv with the lat. and long.
    df.to_csv(output_path, index=False)
    print(f'The file has been updated and saved to {output_path}')
    return output_path
