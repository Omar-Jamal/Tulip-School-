print ("Choose one of the following currencies:")
print ("1.US Dollar")
print ("2.Euro")
print ("3.British Pound")
print ("4.Turkish Lira")
print ("Enter Choice (1/2/3/4)")
choice=input ("your choice is:")
amount=input ("Enter the amount you want to calculate:")
amount=int(amount)

if int(choice) == 1:
    print (f"Euro:{amount*0.822544294}")
    print (f"British Pound:{amount*0.732627569}")
    print (f"Turkish Lira:{amount*7.41245886}")
if int(choice) == 2:
    print (f"US Dollar : {amount*1.21839}")
    print (f"British Pound : {amount*0.891388563}")
    print (f"Turkish Lira : {amount*8.99944566}")
if int(choice) == 3:
    print (f"US Dollar :{amount*1.366845}")
    print (f"Euro : {amount*1.12184522}")
    print (f"Turkish Lira : {amount*10.0936743} ")
if int(choice) == 4:
    print (f"US Dollar : {amount*0.135416}")
    print (f"Euro : {amount*0.111143394}")
    print (f"British Pound : {amount*0.0990719504}")
