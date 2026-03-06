'''Coordinates Program
By Grace LeVoir
3 - 6 - 26'''


# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

try:
    x1 = float(input('Enter the x1 coordinate: '))
    y1 = float(input('Enter the y1 coordinate: '))
    z1 = float(input('Enter the z1 coordinate: '))

    x2 = float(input('Enter the x2 coordinate: '))
    y2 = float(input('Enter the y2 coordinate: '))
    z2 = float(input('Enter the z2 coordinate: '))


    coords_1 = (x1,y1,z1)
    coords_2 = (x2,y2,z2)


    def find_distance(coords_1, coords_2):
        distance = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**(1/2)
        return distance

    distance = find_distance(coords_1, coords_2)
    print(f'The distance is {distance:.2f}')

except:
    print('An error occurred. Please try again.')