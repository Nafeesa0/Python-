#main.py

from Math_operations.Basic_operations import arithmetic

from Math_operations.Geometry import area



print("Arithmetic Oprtaions:")
print("5 + 3 =", arithmetic.add(5,3))
print("10 - 7 =",arithmetic.subtract(10,7))
print("5 * 3 =",arithmetic.multiply(5,3))
print("8 / 2 =",arithmetic.divide(8,2))
print("8 / 0 =", arithmetic.divide(8,0))



print("\nArea Calculation:")
print("Rectangle (length=5, width=3):",area.rectangle_area(5,3))
print("Circle (radius=7):",area.circle_area(7))
print("Triangle (base=4, height=5):",area.triangle_area(4,5))
