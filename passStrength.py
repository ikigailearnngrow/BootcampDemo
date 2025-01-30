
p=input("Enter Password: ")
cp=0
sm=0
sp=0
d=0

for i in p:
    if(i>='A' and i<='Z'):
        cp=cp+1
    if(i>='a' and i<='z'):
        sm=sm+1
    if(int(i)>=0 and int(i)<=9):
        d=d+1
    else:
        sp=sp+1
print("cp=",cp)
print("sm=",sm)
print("d=",d)
print("sp=",sp)
if(len(p)>=8):
    if(cp>=1 and sm>=1 and sp>=1 and d>=1):
        print("Strong")
    elif((cp>=1 and sm>=1) or (sm>=1 and sp>=1) or (sp>=1 and d>=1)\
         or (d>=1 or cp>=1)):
        print("Medium")
    elif(cp>=1 or sm>=1 or sp>=1 or d>=1):
        print("Weak")
else:
    print("Minimum char must be 8")
