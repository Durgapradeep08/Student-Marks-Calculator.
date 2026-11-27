a=int(input ("enter the mark of chemistry")) 
b=int(input ("enter the mark of python")) 
c=int(input ("enter the mark of mechanics"))
totalmark=a+b+c
average=totalmark/3
print("average=",average)
if average>=80:
  print("grade A")
elif average<80 and average>60:
  print("grade B")
else:
  print(C)
