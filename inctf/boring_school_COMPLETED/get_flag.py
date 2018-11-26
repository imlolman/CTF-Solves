import random


while True:
	a=random.randint(1,9)
	b=random.randint(1,9)
	c=random.randint(1,9)


	if(a!=b!=c):
		if((a+b+c)*(a*b*c) == (a*100)+(b*10)+(c*1)):
			print("inctf{"+str((a*100)+(b*10)+(c*1))+"}")
			break


#135 = (1+3+5)*(1*3*5) = 9*15 = 135