print (" Done by OBADA SMAISEM ")

print("choose one of the following numbers ")
print("1. triangle area ")
print("2. square area ")
print("3. circle area ")
print("enter choice (1,2,3)")
choice= int(input("your choice is :"))
if choice == 1:   
  a = float(input("enter the first length "))  
  b = float(input("enter the second length "))  
  c = float(input("enter the third length "))  
  s = (a+b+c)/2 
  area = (s*(s-a)*(s-b)*(s-c))**0.5  
  print( " the area is : %0.2f " % area)

elif choice == 2:
 (print("calculate square area "))
 length=float(input(" enter side of square "))
 area = length*length
 print("area of square is:" , area)

elif choice == 3:
 (print(" calculate circle area "))
 pi=3.14
 r=float(input(" enter the radious of the circle : "))
 area = pi*r*r
 print("area of circle is " ,area )
