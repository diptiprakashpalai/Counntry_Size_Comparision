import matplotlib.pyplot as plt

# Define Axis and Figure
fig, ax = plt.subplots()

# Scale the axis to a size appropriate for the desired circle
# xlim and ylim arguments set to the upper and lower bounds of the x and y axes.
ax.set(xlim=(-1, 1), ylim = (-1, 1))

# Create a circle with center (x,y) and radius r
a_circle = plt.Circle((0, 0), 1, fill = False)
b_circle = plt.Circle ((0, 0), 2, fill = False)

# add Circle to the axis 
ax.add_patch(a_circle)
ax.add_patch(b_circle)

plt.show()