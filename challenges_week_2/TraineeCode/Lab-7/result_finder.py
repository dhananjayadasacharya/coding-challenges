class ResultFinder:
    """
    Properties of the fields of this class
    """
    def __init__(self):
        self.marks1 = 0
        self.marks2 = 0
        self.marks3 = 0

    """
    Method to display marks obtained
    """
    def display_marks(self):
        print("Marks 1 : " + str(self.marks1))
        print("Marks 2 : " + str(self.marks2))
        print("Marks 3 : " + str(self.marks3))

    """
    Method to get the total of the marks in subjects
    """
    def get_total(self):
        return self.marks1 + self.marks2 + self.marks3

    """
    Method to calculate the average of the marks
    """
    def get_average(self):
        return round(self.get_total()/3,2)

    """
    Method to get the result for the marks given
    """
    def get_result(self):
        # Pass criteria: all marks >= 40 and average >= 50
        if self.marks1 >= 40 and self.marks2 >= 40 and self.marks3 >= 40 and self.get_average() >= 50:
            return "Pass"
        else:
            return "Fail"
