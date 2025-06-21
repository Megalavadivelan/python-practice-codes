A=int(input("Tamil:"))
B=int(input("English:"))
C=int(input("Maths:"))
D=int(input("Science:"))
E=int(input("Social:"))
F=(A+B+C+D+E)/5
if(F<35):
    print("Additional class is required")
else:
    print("You are good to go")
