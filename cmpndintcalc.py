#compound intrest calculator
p,r,t,n = 0,0,0,0
while p <= 0:
    p = float(input("Enter the principal amount : "))
    if p <= 0:
        print("principal cannot be less than or equal to 0")
while r <= 0:
    r = float(input("Enter the rate of intrest : "))
    if r <= 0:
        print("intrest Rate cannot be less than or equal to 0")
while t <= 0:
    t = int(input("Enter the time in years : "))
    if t <= 0:
        print("time cannot be less than or equal to 0")
while n <= 0:
    n = int(input("enter number of times intrest to be compounded each year : "))
    if n <= 0:
        print("compound frequency cannot be less than or equal to 0")


amount = p*(1 + r/(100*n))**(n*t)
print(f"total amount after {t} years is : {amount:+,.2f}")