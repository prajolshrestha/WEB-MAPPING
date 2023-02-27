# WEB-MAPPING

#Volcano Map using Folium
This project is a simple implementation of volcano map using the Folium library. The map shows locations of volcanoes in the United States and their respective elevation levels. It also displays a population heatmap based on the population in different areas.

#Prerequisites
Before running this project, make sure you have the following installed:

Python 3
Pandas
Folium
Jupyter Notebook or any other Python editor

#Running the project
Download or clone the repository to your local machine.
Run volcano_map.py file.
The map will be saved as an HTML file named Map1.html in the same directory.

#Understanding the code
The code begins by importing necessary libraries and reading the Volcanoes.txt file containing information about the volcanoes. It reads the latitude, longitude, elevation, and name of the volcanoes from the file and stores them in separate lists.

The map object is created using the Map class provided by the Folium library. The location and zoom level of the map are set, and the base layer of the map is added.

Next, a function color_generator is defined that takes the elevation of a volcano as input and returns a color based on its elevation. This function is used to color the markers representing the volcanoes.

A FeatureGroup layer is created for the volcanoes, and for each volcano, a circular marker is added to the layer with a popup message showing its name, height, and a link to Google search. The color of the marker is set based on the elevation of the volcano.

Another FeatureGroup layer is created for the population, and a polygon is added to the layer representing the population in different areas. The color of the polygon is set based on the population in that area.

Finally, the feature groups are added to the map object, and the LayerControl object is added to control the visibility of each layer. The map is then saved as an HTML file.

#Conclusion
This project shows how easy it is to create interactive maps using the Folium library in Python. With this project as a starting point, you can build more complex and informative maps by exploring different features of the Folium library.

#Credits
This motion detector app was built by PRAJOL SHRESTHA as a personal project. 
If you have any feedback or suggestions, feel free to create a pull request or contact me via email.

#License
This motion detector app is licensed under the MIT License. You are free to use, modify, and distribute this application as long as you give credit to the original author.
