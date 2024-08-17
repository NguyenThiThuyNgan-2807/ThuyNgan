import math
a = float (input("a = "))
b = float (input("b = "))
c = float (input("c = "))
d = b**2 - 4*a*c

#Giải phương trình bậc nhất:
print ("Giải phương trình bậc nhất: ax + b = 0")
if a==0:
    if b==0:
        print ("Phương trình bậc nhât có vô số nghiệm.")
    else:
        print ("Phương trình bậc nhất vô nghiệm.")
else:
    print ("Phương trình bậc nhất có 1 nghiệm duy nhất.")
    
#Giải phương trình bậc hai:
print ("Giải phương trình bậc hai: ax^2 + bx + c = 0")
if a==0:
    if b==0:
        if c==0:
            print ("Phương trình có vô số nghiệm.")
else:
    if d<0:
        print ("Phuơng trình bậc hai vô nghiệm.")
    elif d == 0:
        print ("Phương trình bậc hai có nghiệm kép x1 = x2 = ", -b/(2*a))
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print ("Phương trình bậc hai có 2 nghiệm phân biệt ", x1, x2)



    
