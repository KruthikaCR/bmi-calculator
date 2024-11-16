print("This is a BMI Calculator\n")
name=input("Enter your name : ")
weight=float(input("Enter your weight :"))
height=float(input("Enter your height :"))
BMI= weight/(height/100)**2
if BMI < 18.5:
    print("You're underweight.")
elif 18.5 <= BMI < 25:
    print("You're normal weight.")
elif 25 <= BMI < 30:
    print("You're overweight.")
else:
    print("You're obse.")