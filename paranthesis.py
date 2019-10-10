def checkstring(str1):
    li=[]
    count=0
    li=list(str1)
    for i in li:
        if i is '(':
            count+=1
        elif i is ')':
            count-=1
        elif i is '[':
            count+=2
        elif i is ']':
            count-=2
        elif i is '{':
            count+=3
        elif i is '}':
            count-=3
        else:
            pass

    if(count==0):
        print("Balanced")
    else:
        print("Not Balanced")
            
    
checkstring('[](){}')
checkstring("()[{)}")
checkstring("()")
