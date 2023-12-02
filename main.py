


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

def day2():
    data = open("day2.txt","r")
    sum=0
    for x in data:
        idd=int(x[x.find(" ")+1:x.find(":")])
        power=0
        r,g,b=0,0,0
        minr,ming,minb=1,1,1
        start = x.find(":")
        end=x.find(";")
        if(end==-1):
            end=len(x)
        while(start<len(x)):
            if x.find("red",start,end)!=-1:
                q=x.find("red",start,end)
                r=int(x[x.find(" ",q-4,q):q-1])
            if x.find("green", start, end) != -1:
                q = x.find("green", start, end)
                g = int(x[x.find(" ", q - 4, q):q - 1])
            if x.find("blue", start, end) != -1:
                q = x.find("blue", start, end)
                b = int(x[x.find(" ", q - 4, q):q - 1])
            minr = max(r,minr)
            ming = max(g, ming)
            minb = max(b, minb)
            start=end
            end = x.find(";",start+1)
            if (end == -1):
                end = len(x)

        power = minr * minb * ming
        sum = sum + power

    print(sum)
    return 0

#day1()
day2()

