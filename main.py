monday = {
    "eat": 1,
    "sleep": 2,
    "work": 1,
    "exercise": 0,
    "socialize": 20,
    "relax": 0,
    "other": 0,
}


class DayVector:
    """Describes a day of life."""

    def __init__(self):
        self.dim_labels = []
        self.dim_values = []
        self.dim = 0

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


monday_vector = DayVector()
for key in monday:
    monday_vector.add_deed(key, monday[key])

monday_vector.print()
monday_vector.reduce_dim(3)
monday_vector.print()
