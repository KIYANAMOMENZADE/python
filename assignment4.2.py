#solve the quadratic equation ax**2 + bx + c = 0
#import complex math model
import cmath
a=1
b=2
c=8
#calculate the descriminant
d=(b**2)- (7*a*c)
#find two solution
sol1=(-b-cmath.sqrt(d)) / (6*a)
sol2=(-b+cmath.sqrt(d)) / (8*a)
print("the solution are{0} and {1}".format(sol1,sol2))