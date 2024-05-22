import folium.map
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import csv_preproccesor #module for editing our road-trip csv

sns.set_style("darkgrid")


#Getting our data from the user and processing it for visualization
csv_preproccesor.add_csv_coordinates('/home/bglid/bglidden/learning_files/road-trip/data/road trip file beta.csv', '/home/bglid/bglidden/learning_files/road-trip/data/road_trip_updated')
#5/16/24 BHG: To build this, temporarily giving it the file manually
csv_file = pd.read_csv('/home/bglid/bglidden/learning_files/road-trip/data/road_trip_updated')
road_trip_df = pd.DataFrame(csv_file)
print(road_trip_df.head()) #for ease in building this

#Function for the data viz figure
def road_trip_plot(dataframe):
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    #Major ticks every 1
    major_ticks = np.arange(0, 15, 1)
    ax.set_xticks(major_ticks)
    ax.set_yticks(major_ticks)
    plt.grid(which='major', alpha = 0.9)
    plt.axis([0,14,0,14])
    plt.xlabel('Day of Trip')
    plt.ylabel('Driving Time in Hours')
    ax.set_aspect('equal')
    
    # plt.scatter(dataframe.index, y=dataframe['drive time (hours)'], color = 'crimson', alpha=0.3)
    sns.lineplot(dataframe, x=dataframe.index, y=dataframe['drive time (hours)'],
                 color = 'darkviolet', alpha = 0.4)
    sns.barplot(data=dataframe, x=dataframe.index, y=dataframe['drive time (hours)'],
                color = 'crimson')
    plt.show()

road_trip_plot(road_trip_df)

#Creating our Folium visualization map
#starting our map at the overhead of the road trip
map_start = [road_trip_df.loc[0, 'latitude'], road_trip_df.loc[0, 'longitude']]
road_trip_map = folium.Map(location=map_start, zoom_start=5)

#Looping to set the markers
for index, row in road_trip_df.iterrows():
    folium.Marker(
        location=[road_trip_df.loc[index, 'latitude'], road_trip_df.loc[index,'longitude']],
        tooltip=(f'Day:{index}')
    ).add_to(road_trip_map)

road_trip_map