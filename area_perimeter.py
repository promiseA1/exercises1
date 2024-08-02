from math import pi
def area_perimeter_of_a_circle(radius , pi):
    return f"The area of a circle is {round(area , 2)} and perimeter is {round(perimeter , 2)}"

radius = 5.5
area = radius * radius * pi
perimeter = 2 * radius * pi
print(area_perimeter_of_a_circle(radius , pi))