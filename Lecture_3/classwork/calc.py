import shape

def main():
	s = shape.Square(5)	
	print(s.area())

	r = shape.Rectangle(5, 10)
	print(r.perimeter())

if __name__ == "__main__":
	main()