# model.py
# Agents!
#
# Define a number of Agents, each with a random x and y coordinate
# Cycle through a number of iterations
# For each iteration randomly move the agent by 1 unit in each direction
# Calculate the final distance between all the agents
# Plot the final agent positions using Matplotlib.pyplot

import operator
import matplotlib.pyplot
import agentframework

# function to determine distance between two agents
def distance_between(agents_row_a, agents_row_b):
    dy=agents_row_b.y-agents_row_a.y
    dx=agents_row_b.x-agents_row_a.x
    return((dx**2+dy**2)**0.5)  

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents
for i in range(num_of_agents):        
    agents.append(agentframework.Agent())

# Move the agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

# Plot agent locations
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color="blue")

# Distance between all agents (redundant)
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

# Distance between all agents stored in a list
# Do not include repeated pairings or self pairings
mat=[]

for i in range(num_of_agents-1):            # rows
    for j in range(i+1,num_of_agents):      # columns
        distance=distance_between(agents[i], agents[j])
        mat.append([i,j,distance])

# Maximum and Minimum distance between two agents
dmax = max(mat, key=operator.itemgetter(2))
dmin = min(mat, key=operator.itemgetter(2))

# Plot maximum and minimum pairs
print("\nmax distance is ",dmax[2],"between agents",dmax[0],"and",dmax[1])
matplotlib.pyplot.scatter(agents[dmax[0]].x,agents[dmax[0]].y,color="red")
matplotlib.pyplot.scatter(agents[dmax[1]].x,agents[dmax[1]].y,color="red")

print("\nmin distance is ",dmin[2],"between agents",dmin[0],"and",dmin[1])
matplotlib.pyplot.scatter(agents[dmin[0]].x,agents[dmin[0]].y,color="green")
matplotlib.pyplot.scatter(agents[dmin[1]].x,agents[dmin[1]].y,color="green")

matplotlib.pyplot.show()



