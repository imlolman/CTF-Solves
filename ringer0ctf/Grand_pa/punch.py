
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lis = list(letters)

def getword(numrow, toprow):
	if(numrow == "A"):
		return " "
	if(toprow == 0):
		return numrow
	return lis[(int(numrow)+(9*(int(toprow)-1))) - 1];

triggers = list("1211211212113000303312012112100003011120001111110001100")
codes    = list("6317A42A95457837A1351326317A24938A1342A8311244616281331")

i = 0
for t in triggers:
	print getword(codes[i],triggers[i]),
	i+=1