import math as M
# x = float(input("enter radius"))
# y = 4
# e = 3.5435645
# f = 3.14
# h = -42.25
# h = abs(h)
# j =round(e)
# k =round(f)
# z = pow(x,y)
# result = max(x,y,z,e,f,h)
# print(result)
# print(z,e,f,h)
# print(round(M.pi,4))#3.1415926....->3.1416
# print(M.e)
# #result = M.sqrt(x)
# print(result)
#math -> ceil Fn will always round a float number up 
# result1,result2 = M.ceil(e),M.ceil(f)
# print("e , f using ceil are =",result1,result2,"while rounded e,f =",j,",",k)
# circumference = 2*M.pi*x
# area = M.pi*(pow(x,2))# pi*x**2,pi*x*x both also work 
# print(f"circumference of the circle with radius {x} is : {circumference} and area is {area}")
a = float(input('enter side A '))
b = float(input('enter side B '))
#c = float(input('enter side C '))
c = M.sqrt(pow(a,2) + pow(b,2))
print(c)
s = (a+b+c)/2
area = M.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
