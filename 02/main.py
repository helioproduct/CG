import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


class Prism:
    def __init__(self, center, side_length, height):
        self.center = np.array(center)
        self.side_length = side_length
        self.height = height
        self.vertices = self._create_vertices()
        self.edges = self._create_edges()

    def _create_vertices(self):
        # Calculate the vertices of the base octagon
        angle = 2 * np.pi / 8
        base_vertices = [
            self.center[:2]
            + self.side_length * np.array([np.cos(i * angle), np.sin(i * angle)])
            for i in range(8)
        ]

        # Add height to create the top vertices
        top_vertices = [np.append(v, self.height) for v in base_vertices]
        base_vertices = [np.append(v, 0) for v in base_vertices]

        return base_vertices + top_vertices

    def _create_edges(self):
        edges = []
        # Add edges for the base and top octagon
        for i in range(8):
            edges.append((i, (i + 1) % 8))  # Base
            edges.append((i + 8, (i + 1) % 8 + 8))  # Top

        # Add vertical edges
        for i in range(8):
            edges.append((i, i + 8))

        return edges

    def draw(self, ax, projection="orthographic"):
        # Draw edges
        for edge in self.edges:
            p1, p2 = self.vertices[edge[0]], self.vertices[edge[1]]
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color="b")

        # Set plot limits and labels
        ax.set_xlim(-2 * self.side_length, 2 * self.side_length)
        ax.set_ylim(-2 * self.side_length, 2 * self.side_length)
        ax.set_zlim(-self.height, 2 * self.height)
        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        ax.set_zlabel("Z axis")

        # Apply projection if needed
        if projection == "isometric":
            angle = 45
            ax.view_init(30, angle)


# Create a prism and plot it
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")
prism = Prism(center=[0, 0], side_length=1, height=2)
prism.draw(ax, projection="isometric")
plt.show()
