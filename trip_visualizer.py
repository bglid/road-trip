import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import csv_preproccesor #module for editing our road-trip csv
sns.set_style("darkgrid")



#Getting our data from the user and processing it for visualization
#5/16/24 BHG: To build this, temporarily giving it the file manually
csv_file = pd.read_csv('/home/bglid/bglidden/learning_files/road-trip/data/road_trip_updated')
road_trip_df = pd.DataFrame(csv_file)
print(road_trip_df.head()) #for ease in building this

#Doing Data Visualization on the data
# sns.histplot(data=road_trip_df, x=road_trip_df['Date'], y=road_trip_df['drive time (hours)'],
#              color = 'darkviolet')
plt.scatter(road_trip_df['Date'], y=road_trip_df['drive time (hours)'], color = 'darkviolet')
plt.show()

#Creating our Folium visualization