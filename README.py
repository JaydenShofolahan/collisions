#Name: Jayden 
#Date: 11/09/2024 
#Description: This program will map collisions from a user 

import folium 
import pandas 

file = input("Enter a csv file") 
output = input("Enter an output of the file name") 

collides = pd.read_csv(file) 

mapCollide = folium.Map(location=[40.768731, -73.964915])

for index, row in collides.interrows():
  latitude = row["LATITUDE"] 
  longitude = row["LONGITUDE"] 
  place = row["LOCATION"] 
  ano_place = folium.Marker([latitude, longitude], popup=place) 
  ano_place.add_to(mapCollide) 

mapCollide.save(outsave = output) 