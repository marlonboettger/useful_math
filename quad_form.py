def quad_form(a, b, c):
	"""Function to calculate the Quadratic formula, descrinig the solutions of a quadratic equation: https://en.m.wikipedia.org/wiki/Quadratic_formula"""
	import math
	b_power_2 = math.pow(b,2)
	four_ac = 4*a*c
	discr = b_power_2 - four_ac
	num = 2*a
	
	if discr>0:
		print("Discriminant larger than zero.")
		discr_sqrt = math.sqrt(discr)
		first_root = -b+discr_sqrt/num
		scnd_root = -b-discr_sqrt/num
		if first_root<scnd_root:
			print("The first root is", first_root,
			"The second root is", scnd_root)
		else:
			print("The first root is", scnd_root,
			"The second root is", first_root)
	elif discr==0:
		real_root = -b/num
		print("The discriminant is equal to zero, therefore the solution is:", real_root)
	else:
		print("Discriminant less than zero, therefore there are no real roots.")