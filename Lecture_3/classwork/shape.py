class Shape:
	def area(self):
		return 0
	def perimeter(self):
		return 0

class Rectangle(Shape):
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth

	def area(self):
		return self.length * self.breadth

	def perimeter(self):
		return 2 * (self.length + self.breadth)

class Square(Rectangle):
	def __init__(self, side):
		Rectangle.__init__(self, side, side)
		print(id(self))
		print(id(super()))
		

