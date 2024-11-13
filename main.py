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

    def print(self):
        for i in range(self.dim):
            print(self.dim_labels[i], self.dim_values[i])
