import graphics
from matplotlib import pyplot as plt

TITLE = "What if your day was a vector .. ?"
fig = plt.figure()
fig.tight_layout()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlim(0, 2)
ax.set_title(TITLE)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")


class DayVector:
    """Describes a day of life."""

    def __init__(self):
        self.dim_labels = []
        self.dim_values = []
        self.dim = 0
        self.color = "yellow"
        self.name = "default"

    def add_deed(self, label, value):
        self.dim_labels.append(label)
        self.dim_values.append(value)
        self.dim += 1

    def reduce_dim(self, new_dim):
        """Reduce the dimension of the day vector by removing the least important deeds."""
        if new_dim >= self.dim:
            return
        while self.dim > new_dim:
            min_value = min(self.dim_values)
            min_index = self.dim_values.index(min_value)
            self.dim_labels.pop(min_index)
            self.dim_values.pop(min_index)
            self.dim -= 1

    def normalize(self):
        """Normalize the day vector."""
        total = sum(self.dim_values)
        for i in range(self.dim):
            self.dim_values[i] /= total

    def print(self):
        output = ""
        output += "Day vector: transpose("
        for i in range(self.dim):
            output += str(self.dim_values[i]) + ", "
        print(
            output
            + ") "
            + "element of "
            + str([i for i in self.dim_labels])
            + " basis."
        )

    def plot(self, ax):
        """Plot the day vector in 3D space."""
        self.reduce_dim(3)
        self.normalize()
        dim1, dim2, dim3 = self.dim_values if len(self.dim_values) == 3 else (0, 0, 0)
        ax.arrow3D(
            0,
            0,
            0,
            dim1,
            dim2,
            dim3,
            mutation_scale=20,
            arrowstyle="-|>",
            linestyle="dashed",
            fc=self.color,
            ec="black",
        )
        ax.annotate3D(
            "point 1", (dim1, dim2, dim3), xytext=(3, 3), textcoords="offset points"
        )


monday = {
    "eat": 1,
    "sleep": 2,
    "work": 1,
    "exercise": 0,
    "socialize": 20,
    "relax": 0,
    "other": 0,
}
tuesday = {
    "eat": 1,
    "sleep": 10,
    "work": 4,
    "exercise": 1,
    "socialize": 1,
    "relax": 1,
    "other": 1,
}
monday_vector = DayVector()
for key in monday:
    monday_vector.add_deed(key, monday[key])

monday_vector.print()
monday_vector.reduce_dim(3)
monday_vector.print()


monday_vector.plot(ax)
tuesday_vector = DayVector()
tuesday_vector.color = "blue"
for key in tuesday:
    tuesday_vector.add_deed(key, tuesday[key])
tuesday_vector.plot(ax)

plt.show()
