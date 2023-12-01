


def firstandlast(s):
    a,b=0,0
    aval,bval=0,0
    for i in range(0,len(s)):
        if(ord("0")<=ord(s[i])<=ord("9")):
            a=i
            aval=int(s[i])
            break;
    for j in range(len(s)-1,-1,-1):
        if (ord("0")<=ord(s[j])<=ord("9")):
            b = j
            bval=int(s[j])
            break;
    N=["one","two","three","four","five","six","seven","eight","nine"]
    for x in range(0,len(N)):
        k=s.find(N[x])
        l=s.rfind(N[x])
        if k!=-1 and k<a:
            a=k
            aval=x+1
        if l!=-1 and l>b:
            b=l
            bval=x+1

    return (aval*10)+bval

def day1():
    data = open("day1.txt","r")
    sum=0
    for i in data:
        sum=sum+firstandlast(i)
    print(sum)
    data.close()
    return 0


#day1()

