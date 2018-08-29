import math 

'''Calculator that takes input from the user and calculates the area 
of a square, rectangle, parallelogram, triangle, trapezoid and circle.''' 

def calc_sq(side):
	square_area = math.pow(side,2)
	return square_area
	
def calc_rec(side_1, side_2):
	rec_area = side_1 * side_2
	return rec_area
	
def calc_par(b,h):
	par_area = b*h
	return par_area
	
def calc_tri(base, height):
	tri_area = (base*height)/2
	return tri_area
	
def calc_trap(hei, b_1, b_2):
	trap_area = ((b_1 + b_2)/2)*hei
	return trap_area
	
def calc_cir(radius):
	cir_area = math.pi*math.pow(radius,2)
	return cir_area
	
while True: 
	try:
	
		question1 = raw_input("What would you like to do?\n\n(square, rectangle, parallelogram, triangle, trapezoid or circle?) ")
	
		if question1 == 'square':
			side = float(raw_input("Input the side of the square: "))
			print calc_sq(side) 

		elif question1 == 'rectangle':
			side_1 = float(raw_input("Input the first side of the rectangle: "))
			side_2 = float(raw_input("Input another one: "))
			print calc_rec(side_1, side_2) 

		elif question1 == 'parallelogram':
			b = float(raw_input("Input the base: "))
			h = float(raw_input("Input the height: "))
			print(calc_par(b,h))
	
		elif question1 == 'triangle':
			base = float(raw_input("Input the base: "))
			height = float(raw_input("Input the height: "))
			print(calc_tri(base, height))
	
		elif question1 == 'trapezoid':
			hei = float(raw_input("Input the height: "))
			b_1 = float(raw_input("Input the first base: "))
			b_2 = float(raw_input("Input the second base: "))
			print(calc_trap(hei, b_1,b_2))
	
		elif question1 == 'circle':
			radius = float(raw_input("Input the radius: "))
			print(area_cir(radius))
			radius = float(raw_input("Input the radius: "))
			print(calc_cir(radius))
		
		else: 
			print("Error, please try again.")
			
		stop = raw_input("Continue? Yes or no?\n...")
		if stop == 'no':
			break
	
	except ValueError:
		print("Not a legible answer. Please try again...")

	
	