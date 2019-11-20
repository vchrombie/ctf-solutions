import string
import random

def push(x):
    
	upper = string.ascii_uppercase
	lower = string.ascii_lowercase
	digits = string.digits
	n = []
	a = ""
	for i in x:
		if i.isupper() is True:
			n.append(upper[(upper.index(i)+3)%26])
		elif i.islower() is True:
			n.append(lower[(lower.index(i)+3)%26])
		elif i.isdigit() is True:
			n.append(digits[(digits.index(i)+3)%10])
	
	for j in n:
		a+=j

	return a
    

def sage(x): 
	final=[] 
	for i in range(0,len(x),4):
		temp=x[i:i+4].encode('utf-8').hex()
		k=int(temp,16)
		final.append(k)
    
	return final

if __name__=="__main__":
	
	print("Get the flag if you can!")																	 																								
	x = input().encode('utf-8').hex()
	check = [959592808, 959852599, 960049253, 926430775, 892811314, 946419251, 929576502, 946419765, 909391664, 925972535, 892613940, 912864564, 12391]
	ALL = []
	ALL=sage(push(x))
	count = 0

	for i in range(len(ALL)):
		if check[i] == ALL[i]:
			count+=1
	if count == 13:
		print("Go Kid Submit The Flag")
	else:
		print("Wrong Turn!")
