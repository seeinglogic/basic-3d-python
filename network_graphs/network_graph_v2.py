import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


# Chosen by random dice roll
seed = 4
np.random.seed(seed)

# Generate a random graph
G = nx.erdos_renyi_graph(n=30, p=0.2, seed=seed)

# Use nx to do a 3d-layout
pos = nx.spring_layout(G, dim = 3, k = 0.5) # k regulates the distance between nodes

# Calculate the Euclidean distance of each node from the origin
distances = np.array([np.sqrt(x**2 + y**2 + z**2) for x, y, z in pos.values()])

# Scale the distances to lie between 0 and 1 for color mapping
distance_colors = distances / max(distances)

# Plot the graph in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot nodes with color scaled by distance from the origin and size scaled by degree
x = np.array([pos[v][0] for v in G])
y = np.array([pos[v][1] for v in G])
z = np.array([pos[v][2] for v in G])

#scatter = ax.scatter(x, y, z, c=distance_colors, cmap='viridis', s=200)  # Color nodes based on distance
scatter = ax.scatter(x, y, z, c=distance_colors, cmap='plasma', s=200)  # Color nodes based on distance

# Plot edges
for edge in G.edges():
    x = np.array([pos[edge[0]][0], pos[edge[1]][0]])
    y = np.array([pos[edge[0]][1], pos[edge[1]][1]])
    z = np.array([pos[edge[0]][2], pos[edge[1]][2]])
    ax.plot(x, y, z, c="tab:gray")

plt.show()
