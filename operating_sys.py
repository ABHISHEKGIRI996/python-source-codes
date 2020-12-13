#operating system
import os



ch=input("TO know the current folder path press (y/n)")
if ch=="y" or ch=="Y" :
    print(os.getcwd())
else:
    print("press yes to khow the current folder path ")

print("please create new directory to start your work ")
name=input("enter any name to make directory : ")

if os.path.exists(name):
    print("file already exits !!!")
else:
    os.mkdir(name)
    print("A new file created in the name of ",name)





