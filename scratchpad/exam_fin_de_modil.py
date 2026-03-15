######2######
import math
n = int(input("donnez n"))
s=0
while(1==1):
    a=int(input("donner le nomber"))
    for i in range(1, a + 1):
        s=s+math.cos(1+i)/(1+i*i)
        print("S=", s)
    if(i>=n):
        break


