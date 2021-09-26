class Grades:
	def __init__(self, semester) -> None:
	    self.semester = semester
	    self.grades = list()
	
	def addGrade(self, courseName, courseFinalCalification):
		self.grades.append(
			{
				"courseName": courseName,
				"courseFinalCalification": courseFinalCalification
			}
		)
		return self