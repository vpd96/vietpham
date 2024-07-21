
class Student():
	point = []
	def __init__(self):
		self.point = []
	def insert_point(self, p1):
		self.point.append(p1)
	def avg_cal(self):
		i = 0
		sum = 0
		for x in self.point:
			i += 1
			sum +=x
		return sum/i

stu = Student()
stu.insert_point(7)
stu.insert_point(7)
stu.insert_point(8)

print("avg_point: ", stu.avg_cal())