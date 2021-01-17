units=int(input("please enter the number of units you consumed in a month"))
if(units<=100):
    payAmount=units*2.60
    fixedcharge=25.00
elif(units<=200):
    payAmount=(100*2.60)+(units-100)*3.80
    fixedcharge=35.00
elif(units<=300):
    payAmount=(100*2.60)+(200-100)*3.80+(units-200)*4.25
    fixedcharge=75.00
elif(units<=400):
    payAmount=(100*2.60)+(200-100)*3.80+(300-200)*4.25+(units-300)*5.00
    fixedcharge=60.00
else:
    payAmount=0
    fixedcharge=1570
Total=payAmount+fixedcharge;
print("\nElecticity bill=%.2f"%Total)
