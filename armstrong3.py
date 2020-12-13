#armstrong 3
no=input("ENTER ANY INYEGER : ")
ln=len(no)
s=0
for i in range (0,ln):
    s=s+int(no[i])**ln
if(s==int(no)):
    print("THIS NUMBER IS A ARMSTRONG NUMBER ")
else :
    print("THIS NUMBER IS NOT A ARMSTRONG NUMBER ")
    
