# model.py
#
# Agents!
#
# Create a number of Agents, each with a random x and y coordinate (0-99).
# Cycle through a number of iteration steps.
# For each iteration randomly move the agent by +/- 1 unit in each direction.
# The agent must stay within the bounds of the model 0-99.
# If the agent steps below 0 its position is shifted to 99.
# If the agent steps above 99 its position is shifted to 0.
# Calculate the final distance between all the agents.
# Plot the final agent positions using Matplotlib.
# Highlight the two closest Agents and the two furthest Agents

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

# Make the agents using the Agent class
for i in range(num_of_agents):        
    agents.append(agentframework.Agent())

# Move the agents using the move method
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

# Plot agent locations
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color="blue")


# Distance between all agents stored in a list
# Do not include repeated pairings or self pairings
mat=[]

for i in range(num_of_agents-1):            
    for j in range(i+1,num_of_agents):      
        distance=distance_between(agents[i], agents[j])
        mat.append([i,j,distance])

# Maximum and Minimum distance between two agents
dmax = max(mat, key=operator.itemgetter(2))
dmin = min(mat, key=operator.itemgetter(2))
print("\nmax distance is ",dmax[2],"between agents",dmax[0],"and",dmax[1])
print("\nmin distance is ",dmin[2],"between agents",dmin[0],"and",dmin[1])

# Plot maximum and minimum pairs
matplotlib.pyplot.scatter(agents[dmax[0]].x,agents[dmax[0]].y,color="red")
matplotlib.pyplot.scatter(agents[dmax[1]].x,agents[dmax[1]].y,color="red")

matplotlib.pyplot.scatter(agents[dmin[0]].x,agents[dmin[0]].y,color="green")
matplotlib.pyplot.scatter(agents[dmin[1]].x,agents[dmin[1]].y,color="green")

matplotlib.pyplot.show()



