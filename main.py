


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

def issymbol(s):
    if s=="." or s=="0" or s=="1" or s=="2" or s=="3" or s=="4" or s=="5" or s=="6" or s=="7" or s=="8" or s=="9":
        return False
    else:
        return True

def getnum(s,pos):
    num=""
    i=pos
    j=pos+1
    while i>-1 and s[i].isdigit():
        num=s[i]+num
        i=i-1
    while j<len(s) and s[j].isdigit():
        num=num+s[j]
        j=j+1
    return int(num)

def day3part1():
    N=140
    S=["" for _ in range(0,N)]
    data= open("day3.txt","r")
    sum=0
    k=0
    for x in data:
        S[k]=x
        k=k+1
    for i in range(0,N):
        for j in range(0,N):
            if issymbol(S[i][j]):
                if(S[i-1][j].isdigit()):
                    sum=sum+getnum(S[i-1],j)
                else:
                    if(S[i-1][j-1].isdigit()):
                        sum=sum+getnum(S[i-1],j-1)
                    if (S[i - 1][j + 1].isdigit()):
                        sum = sum + getnum(S[i - 1], j + 1)

                if (S[i + 1][j].isdigit()):
                    sum = sum + getnum(S[i + 1], j)
                else:
                    if (S[i + 1][j - 1].isdigit()):
                        sum = sum + getnum(S[i + 1], j - 1)
                    if (S[i + 1][j + 1].isdigit()):
                        sum = sum + getnum(S[i + 1], j + 1)

                if (S[i][j-1].isdigit()):
                    sum = sum + getnum(S[i], j-1)
                if (S[i][j+1].isdigit()):
                    sum = sum + getnum(S[i], j+1)
    print(sum)
    data.close()
    return 0

def day3part2():
    N=140
    S=["" for _ in range(0,N)]
    data= open("day3.txt","r")
    sum=0
    k=0
    for x in data:
        S[k]=x
        k=k+1
    for i in range(0,N):
        for j in range(0,N):
            if S[i][j]=="*":
                L=[]
                if(S[i-1][j].isdigit()):
                    L.append(getnum(S[i-1],j))
                else:
                    if(S[i-1][j-1].isdigit()):
                        L.append(getnum(S[i-1],j-1))
                    if (S[i - 1][j + 1].isdigit()):
                        L.append(getnum(S[i-1],j+1))

                if (S[i + 1][j].isdigit()):
                    L.append(getnum(S[i+1],j))
                else:
                    if (S[i + 1][j - 1].isdigit()):
                        L.append(getnum(S[i+1],j-1))
                    if (S[i + 1][j + 1].isdigit()):
                        L.append(getnum(S[i+1],j+1))

                if (S[i][j-1].isdigit()):
                    L.append(getnum(S[i],j-1))
                if (S[i][j+1].isdigit()):
                    L.append(getnum(S[i],j+1))
                if len(L)==2:
                    sum=sum+(L[0]*L[1])
    print(sum)
    data.close()
    return 0

def day4():
    data = open("day4.txt","r")
    L=[]
    for x in data:
        a= x.find(":")+1
        b= x.find("|")
        win=[]
        our=[]
        num=""
        amaount=0
        for i in range(a,b):
            if x[i].isdigit():
                num=num+x[i]
            else:
                if num!="":
                    win.append(int(num))
                num=""
        a,b=b+1,len(x)
        for j in range(a,b):
            if x[j].isdigit():
                num=num+x[j]
            else:
                if num!="":
                    our.append(int(num))
                num=""
        for i in win:
            for j in our:
                if(i==j):
                    amaount=amaount+1
        L.append(amaount)
    W=[1 for _ in range(0,len(L))]
    n=len(L)
    sum=0

    for y in range(0,n):
        p=y+1
        while p<n and p<y+L[y]+1:
            W[p]+=1*W[y]
            p+=1
    for o in W:
        sum=sum+o

    print(sum)


    data.close()
    return 0




#day1()
#day2()
#day3part1()
#day3part2()
day4()


