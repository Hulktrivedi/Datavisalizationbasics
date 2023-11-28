# single line chart visualization (Triple quote to triple quote(to run fist example remove the triple quote from the ~
# ~ start and end of the code to uncomment it and comment the other example before running the code))
"""
# A Nutri world-wide firm wants to know how many people visits its website in a particular time. ~
# ~ This analysis helps it control and monitor the website traffic.

# import matplotlib Library
import matplotlib.pyplot as plt
from matplotlib import style

# website traffic data
# number of users/ visitors on the website
web_customers = [123, 645, 950, 1290, 1630, 1450, 1034, 1295, 465, 205, 80]
# Time distribution (hourly)
time_hrs = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# select the style of the plot
style.use('ggplot')
# plot the website traffic data (X-axis hrs and Y axis as number of users)
plt.plot(time_hrs, web_customers)
# set the title of the plot
plt.title('Website traffic')
# set Label for x-axis
plt.xlabel('Hrs')
# set label for y-axis
plt.ylabel('Number of users')
plt.show()
"""

# 2 Dimensional line graph with multiple entity's

# import matplotlib Library
import matplotlib.pyplot as plt
from matplotlib import style

# website traffic data
# number of users/ visitors on the website
# monday web traffic
web_monday = [123, 645, 950, 1290, 1630, 1450, 1034, 1295, 465, 205, 80]
# tuesday web traffic
web_tuesday = [95, 680, 889, 1145, 1670, 1323, 1119, 1265, 510, 310, 110]
# wednesday web traffic
web_wednesday = [105, 630, 700, 1006, 1520, 1124, 1239, 1380, 580, 610, 230]
# Time distribution (hourly)
time_hrs = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# select the style of the plot
style.use('ggplot')
# plot the website traffic data (X-axis hrs and Y axis as number of users)
# plot the monday web traffic with red color
plt.plot(time_hrs, web_monday, 'r', label='monday', linewidth=1)
# plot the monday web traffic with green color
plt.plot(time_hrs, web_tuesday, 'g', label='tuesday', linewidth=1.5),
# plot the monday web traffic with blue color
plt.plot(time_hrs, web_wednesday, 'b', label='wednesday', linewidth=2)
# noinspection PyTypeChecker
plt.axis([6.5, 17.5, 50, 2000])
# set the title of the plot
plt.title('Web site traffic')
# set Label for x axis
plt.xlabel('Hrs')
# set Label for y axis
plt.ylabel('Number of users')
plt.legend()
plt.show()
