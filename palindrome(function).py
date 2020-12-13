#palindrome with function
def pal(no,word):
    ln=len(no)
    no1=int(no)
    r=0
    for i in range (0,ln):
        a=no1%10
        no1=no1//10
        if(a==0):
            r=r*10+no1
        else:
            r=r*10+a

    if(r==int(no)):
        print("GIVEN NUMBER IS PALINDROME !!!!! ",r)
    else:
        print("NUMBER IS NOT PALINDROME ",r)

    w=word[::-1]
    if(w==word):
        print("GIVEN WORD IS PALINDROME !!!!! ",w)
    else:
       print("GIVEN WORD IS NOT PALINDROME !!!!! ",w)
a=input("ENTER ANY INTEGER : ")
word=input("ENTER ANY WORD")
pal(a,word)
