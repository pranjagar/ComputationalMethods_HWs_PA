from turtle import color
import numpy as n
import matplotlib.pyplot as plt

def f(x) :                     # integrand
    return (n.exp(-x**2))
 
#Integrating using the Trapezoidal rule


slices = 100
def E(min,max):
    delx = (max-min)/slices
    Integral=(f(max)-f(min))*delx/2       #non iterative part
    i=0
    while i< slices:
        Integral +=  delx*(f(min + i*delx))      # adding the iterative part
        i = i+1
    return Integral

lower_limit = float(input('Integrate from x = ' ))
upper_limit = float(input('Integrate to x = ' ))
print(f'The integral from {lower_limit} to {upper_limit} is : ', E(lower_limit,upper_limit))


 
# The graphing part:

x_lowerlimit = float(input('Graph from x = ' ))
x_upperlimit = float(input('Graph till x = ' ))
points =int(( x_upperlimit-x_lowerlimit)*50)     # 50 points per unit on x axis

x = n.linspace(x_lowerlimit,x_upperlimit, points)   # x variable list
y = [E(0,i) for i in x]                   # y variable list

plt.plot(x,y, color='b', linestyle = '-')        #plotting
plt.title('Error function plot')
plt.xlabel("x")
plt.ylabel("E(x)")
plt.show()