import graphics
from matplotlib import pyplot as plt

TITLE = "What if your day was a vector .. ?"
fig = plt.figure()
fig.tight_layout()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlim(0, 2)
ax.set_title(TITLE)


class DayVector:
    """Describes a day of life."""

    def __init__(self, name, color, deeds):

        self.dim_labels = []
        self.dim_values = []
        self.dim = 0
        self.color = color
        self.name = name
        for key in deeds:
            self.add_deed(key, deeds[key])

    def add_deed(self, label, value):
        """Adds an entry to the day vector."""
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

    def get_base(self):
        """Get the basis of the day vector."""
        return self.dim_labels

    def set_base(self, new_base):
        """Set the basis of the day vector according to input base."""
        # add deeds of new base to base
        for label in new_base:
            if label not in self.dim_labels:
                self.dim_labels.append(label)
                self.dim_values.append(0)
                self.dim += 1
        # remove deeds not in new base
        for label in self.dim_labels:
            if label not in new_base:
                index = self.dim_labels.index(label)
                self.dim_labels.pop(index)
                self.dim_values.pop(index)
                self.dim -= 1

    def set_axes_labels_to_base(self, axis):
        """Set the axes labels to the basis of the day vector."""
        axis.set_xlabel(self.dim_labels[0])
        axis.set_ylabel(self.dim_labels[1])
        axis.set_zlabel(self.dim_labels[2])

    def print(self):
        """Print the day vector to console."""
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
            self.name, (dim1, dim2, dim3), xytext=(3, 3), textcoords="offset points"
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
tuesday_vector = DayVector("tuesday", "blue", monday)
monday_vector = DayVector("monday", "yellow", tuesday)
tuesday_vector.set_base(monday_vector.get_base())
monday_vector.set_axes_labels_to_base(ax)
monday_vector.plot(ax)
tuesday_vector.plot(ax)


plt.show()
