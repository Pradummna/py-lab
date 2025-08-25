class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {
            "roll": self.roll,
            "name": self.name,
            "marks": self.marks
        }
    
    @staticmethod
    def from_dict(data):
        return Student(
            roll = data["roll"],
            name = data["name"],
            marks = data["marks"]
        )
