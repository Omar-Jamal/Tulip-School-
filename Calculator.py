#This Project is made by: 
# Menna
# Amna
# Arwa
# Gehad
print("Welcome to the Calculator Program")
print("Select an opreation to perform: ")
print()
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print()

while True:
    choice = int(input("Your operation = "))
    if choice == 1:
        num1 = float(input("Enter a number = "))
        num2 = float(input("Enter a number = "))
        summ = num1 + num2
        print("summ is = ",summ)
        break
    elif choice == 2:
        num1 = float(input("Enter a number = "))
        num2 = float(input("Enter a number = "))
        diff = num1 - num2
        print("diff is = ",diff)
        break
    elif choice == 3:
        num1 = float(input("Enter a number = "))
        num2 = float(input("Enter a number = "))
        mul = num1 * num2 …
