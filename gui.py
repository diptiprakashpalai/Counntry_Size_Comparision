from tkinter import *
import requests
import matplotlib.pyplot as plt
import math


country_All = requests.get('https://restcountries.eu/rest/v2/all')
country_list = country_All.json()
length = len(country_list) -1

country_name = []
for i in range(0, length):
    country_name.append(country_list[i]['name'])


# Create object
root = Tk()
root.title('Two Countries Size Comparision')
  
# Adjust size
root.geometry( "400x50" )

country_name1 = StringVar()
country_name1.set(country_name[0]) # default value

country_name2 = StringVar()
country_name2.set(country_name[0]) # default value

w1 = OptionMenu(root, country_name1, *country_name)
w2 = OptionMenu(root, country_name2, *country_name)

w1.pack(side = LEFT, expand = True, fill = BOTH)
w2.pack(side = RIGHT, expand = True, fill = BOTH)

button = Button(root, text="COMPARE", command=root.destroy)
button.pack()

root.mainloop()

#-------------------------------------------------------


country1 = country_name1.get()
country2 = country_name2.get()

country_area = []
for i in range(0, length):
    country_area.append(country_list[i]['area'])
country_area1 = [0 if x == None else x for x in country_area]
#print (country_area1)
#print (max(country_area1))
#print (min(country_area1))

radius = []
for i in range(0, length):
   radius.append(math.sqrt(country_area1[i]/math.pi))
 

for i in range (0, length):
   if country_list[i]['name'] == country1:
      radius_compare1 = radius[i]

for i in range (0, length):
   if country_list[i]['name'] == country2:
      radius_compare2 = radius[i]  


# Define Axis and Figure
fig, ax = plt.subplots()

# Scale the axis to a size appropriate for the desired circle
# xlim and ylim arguments set to the upper and lower bounds of the x and y axes.
ax.set(xlim=(-max(radius), max(radius)), ylim = (-max(radius), max(radius)))

# Hide both the axes
plt.axis('off')

# Hide X & Y Ticks
#plt.tick_params(
#    axis='x',          # changes apply to the x-axis
#   which='both',      # both major and minor ticks are affected
#    bottom=False,      # ticks along the bottom edge are off
#    top=False,         # ticks along the top edge are off
#    labelbottom=False) # labels along the bottom edge are off


# Create a circle with center (x,y) and radius r
a_circle = plt.Circle((0, 0), radius_compare1, fill = False, edgecolor = 'green')
b_circle = plt.Circle ((0, 0), radius_compare2, fill = False, edgecolor = 'red')

# add Circle to the axis 
ax.add_patch(a_circle)
ax.add_patch(b_circle)
plt.legend([country1, country2])

plt.show()

