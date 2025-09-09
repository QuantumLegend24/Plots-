import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[1,2,3,4,5]

plt.plot(x,y)
plt.show()

plt.plot(x,y,"ro")
plt.show()

plt.plot(x,y,"r--")
plt.show()

x=[3,2,8,9,5]
y=[18,21,32,31,43]

plt.plot(x,y)
plt.axis([0,10,0,200])
plt.show()

x=[1,2,3,4,5]
y=[1,2,3,4,5]

plt.plot(x,y,"r--",label="Y=X",linewidth=4)
plt.axis([0,10,0,50])

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Sample Graph")
plt.legend()
plt.show()

x=np.arange(0,10,0.2)
print(x)

y1=x**2
y2=x**3

plt.plot(x,y1,"g--",x,y2,"b--")
plt.show()

m=2#slope
c=1#y-intercept

x=np.linspace(-5,5,100) #generate 100 points between -5 and 5

#Calculate corresponding y values
y=m*x+c

plt.plot(x,y,"b--")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Linear Equation")

plt.show()

#Bar Graph

#x=position of the bar
#y=length of the bar

x=[1,3,5,7]
y=[2,4,6,8]

plt.bar(x,y,color="b")
plt.show()

plt.bar([1,3,5,7],[2,4,6,8],color="b")
plt.bar([2,4,6,8],[3,6,4,1],color="r")

plt.show()

plt.bar(["Male Literacy","Female Literacy"],[90,95])
plt.show()

plt.bar(["Economy","Economy Plus","Business","First","Private"],[37,43,10,8,2])

plt.show()