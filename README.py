#Name: Jayden 
#Date: 11/16/2024 
#Description: This program will map collisions from a user 

import folium 
import pandas 

file = input("Enter a csv file") 
output = input("Enter an output of the file name") 

collides = pd.read_csv(file) 
print(collides["Location"])

mapCollide = folium.Map(location=[0,0], zoom_start = 3)

for index, row in collides.interrows():
  latitude = row["LATITUDE"] 
  longitude = row["LONGITUDE"] 
  place = row["TIME"] 
  ano_place = folium.Marker([latitude, longitude], popup=place) 
  ano_place.add_to(mapCollide) 

mapCollide.save(outfile = output) 
