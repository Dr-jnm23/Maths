from math import sqrt

print('Pythagorean theorem calculator!')
print('Assume sides are a, b, c and c is hypotenuse')
formula = input('Which side (a, b, c) do you wish to calculate? side> ')

if formula == 'c':
	side_a = int(input('Input length of side a: '))
	side_b = int(input('Input length of side b: '))

	side_c = sqrt(side_a * side_a + side_b * side_b)
	
	print('length of side c is: ' )
	print(side_c)

elif formula == 'a':
    side_b = int(input('Input length of side b: '))
    side_c = int(input('Input length of side c: '))
    
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    
    print('length of side a is' )
    print(side_a)

elif formula == 'b':
    side_a = int(input('Input length of side a: '))
    side_b = int(input('Input length of side c: '))
        
    side_c = sqrt(side_c * side_c - side_a * side_a)
    
    print('length of side b is')
    print(side_c)

else:
	print('Please select a side between a, b, c')
	
