salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 or age<=25):
    Loan=int(input("Loan:"))
    if(Loan>=50000):
      print("Maximun loan is 50000")
    else:
      print("you are not eligible")
else:
    print("you are not eligible")
