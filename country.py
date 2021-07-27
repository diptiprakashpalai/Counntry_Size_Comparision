import requests
import matplotlib.pyplot as plt
import math

country_All = requests.get('https://restcountries.eu/rest/v2/all')
country_list = country_All.json()
length = len(country_list) -1
print (length)
country_name1 = input('What is the first country name?')
country_name2 = input('What is the second country name?')
country_area = []
for i in range(0, length):
    country_area.append(country_list[i]['area'])
country_area1 = [0 if x == None else x for x in country_area]
#print (country_area1)
#print (max(country_area1))
#print (min(country_area1))

length1 = len(country_area1) -1
print (length1)
radius = []
for i in range(0, length1):
   radius.append(math.sqrt(country_area1[i]/math.pi))
   
for i in range (0, length):
   if country_list[i]['name'] == country_name1:
      radius_compare1 = radius[i]
      
for i in range (0, length):
   if country_list[i]['name'] == country_name2:
      radius_compare2 = radius[i]

#print (max(radius))
#print (min(radius))
#print (radius)
# Define Axis and Figure
fig, ax = plt.subplots()

# Scale the axis to a size appropriate for the desired circle
# xlim and ylim arguments set to the upper and lower bounds of the x and y axes.
ax.set(xlim=(-max(radius), max(radius)), ylim = (-max(radius), max(radius)))

# Create a circle with center (x,y) and radius r
a_circle = plt.Circle((0, 0), radius_compare1, fill = False, edgecolor = 'green')
b_circle = plt.Circle ((0, 0), radius_compare2, fill = False, edgecolor = 'red')

# add Circle to the axis 
ax.add_patch(a_circle)
ax.add_patch(b_circle)
plt.legend([country_name1, country_name2])

plt.show()