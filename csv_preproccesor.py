import numpy as np
import pandas as pd
from tqdm.auto import tqdm
from geopy.geocoders import Nominatim

#defining our function to get the geolocator per city
def get_location(city, geolocator):
    try:
        location = geolocator.geocode(city)
        return (location.latitude, location.longitude)
    except:
        return (None, None)        

#setting up our dataframe
def csv_preproccesor(file_path, output_path):
    csv = pd.read_csv(file_path)
    df = pd.DataFrame(csv)

    #Instantiating a new Nominatim client
    app = Nominatim(user_agent='road_trip')

    #Getting our latitude and longitude
    tqdm.pandas()
    df['latitude'], df['longitude'] = zip(*df['Route Finish'].progress_apply(lambda x: get_location(x, app)))

    #updating and returning the csv with the lat. and long.
    df.to_csv(output_path, index=False)
    print(f'The file has been updated and saved to {output_path}')
    return output_path
