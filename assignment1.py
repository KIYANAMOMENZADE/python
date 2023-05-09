import math
while True :
    num1 = float(input("enter num1:"))
    op=input("enter op from (radical,sin,cos,tan,factorial)")
    if op=="radical":
        answer=math.sqrt(num1)
        continue
    if op=="sin":
        answer=(math.sin(num1))
        continue
    if op=="cos":
        answer=(math.cos(num1))
        continue
    if op=="tan":
        answer=(math.tan(num1))
        continue
    if op=="factorial":
        if num1>=1:
            print(math.factorial(num1))

    
        
        
