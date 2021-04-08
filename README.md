# agents
 
This program is for the GEOG5003M Agents! practical

The Agents project uses object orientated python to creat an Agent which has a simple x and y coordinate.
When an Agent is created it is initialised with a random x and y integer coordinate between 0 and 99.
The model cycles through a number of iteration steps. For each iteration the Agent is randomly moved by +/- 1 unit in each direction.
The agent must stay within the bounds of the model 0-99. If the agent steps below 0 its position is shifted to 99. If the agent steps above 99 its position is shifted to 0.
After all the iterations are complete the final distance between all the agents is calculated.
The final agent positions are plotted using a Matplotlib scatter plot.
The two closest Agents and the two furthest Agents are highlighted on the scatterplot.

The main program is in model.py. The module containg the Agent class is in agentframework.py

