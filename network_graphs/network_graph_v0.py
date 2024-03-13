# gen by chat
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Step 1: Generate a random graph
G = nx.erdos_renyi_graph(n=30, p=0.2) # n is the number of nodes, and p is the probability of edge creation

# Step 2: Generate random 3D positions for each node
# Create a dictionary to hold positions
pos = {i: (np.random.uniform(), np.random.uniform(), np.random.uniform()) for i in G.nodes()}

# Step 3: Plot the graph in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract the node positions
x = np.array([pos[v][0] for v in G])
y = np.array([pos[v][1] for v in G])
z = np.array([pos[v][2] for v in G])

# Plot nodes
ax.scatter(x, y, z)

# Plot edges
for edge in G.edges():
    x = np.array([pos[edge[0]][0], pos[edge[1]][0]])
    y = np.array([pos[edge[0]][1], pos[edge[1]][1]])
    z = np.array([pos[edge[0]][2], pos[edge[1]][2]])
    ax.plot(x, y, z, c="tab:gray")

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
