


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

class customdik:
    def __init__(self):
        self.dick=[]
    def add(self,k,v):
        self.dick.append([k,tuple((v,v+k[1]-k[0]))])
    def sorter(self):
        self.dick.sort(key=lambda dic: dic[0][0])
        print("A")
        N=len(self.dick)
        if self.dick[0][0][0]!=0:
            self.dick.append([(0,self.dick[0][0][0]-1),(0,self.dick[0][0][0]-1)])
        i=1
        while i<N:
            if self.dick[i][0][1]+1!=self.dick[i+1][0][0]:
                self.dick.append([(self.dick[i][0][1]+1,self.dick[i+1][0][0]-1),(self.dick[i][0][1]+1,self.dick[i+1][0][0]-1)])
                i=i+1
        self.dick.sort(key=lambda dic: dic[0][0])

    def checkrange(self,i):
        N=len(self.dick)
        for x in range(0,N):
            if self.dick[x][0][0]<=i and i<=self.dick[x][0][1]:
                return (self.dick[x][1][0]+(i-self.dick[x][0][0]),x)
        return (i,x)
    def pronter(self):
        for i in range(0,len(self.dick)):
            print(self.dick[i])
    def getranges(self,t):
        R=[]
        a=self.checkrange(t[0])
        b=self.checkrange(t[1])
        if a[1]==b[1]:
            return [(a[0],b[0])]
        if a[1]+1==b[1]:
            return [(a[0],self.dick[a[1]][1][1]),(self.dick[b[1]][1][0],b[0])]
        i=a[1]+1
        end=b[1]
        R.append((a[0],self.dick[a[1]][1][1]))
        while i<end:
            R.append((self.dick[i][1][0],self.dick[i][1][1]))
            i=i+1
        R.append((self.dick[b[1]][1][0],b[0]))
        return R

def day5():
    print("porces start")
    seeds=[(2041142901,113138307),(302673608,467797997),(1787644422,208119536),(143576771,99841043),(4088720102,111819874),(946418697,13450451),(3459931852,262303791),(2913410855,533641609),(2178733435,26814354),(1058342395,175406592)]
    map1=open("seedssoilmap.txt", "r")
    seedsoil=[]
    for x in map1:
        T=[int(x[0:x.find(" ")]),int(x[x.find(" "):x.find(" ",x.find(" ")+1)]),int(x[x.find(" ",x.find(" ")+1):])]
        seedsoil.append(T)
    map1.close()
    map2 = open("soilfertilizermap.txt", "r")
    soilfretilizer = []
    for x in map2:
        T=[int(x[0:x.find(" ")]),int(x[x.find(" "):x.find(" ",x.find(" ")+1)]),int(x[x.find(" ",x.find(" ")+1):])]
        soilfretilizer.append(T)
    map2.close()
    map3 = open("fetilzerwatermap.txt", "r")
    fretilizerwater = []
    for x in map3:
        T = [int(x[0:x.find(" ")]), int(x[x.find(" "):x.find(" ", x.find(" ") + 1)]),
             int(x[x.find(" ", x.find(" ") + 1):])]
        fretilizerwater.append(T)
    map3.close()
    map4 = open("waterlightmap.txt", "r")
    waterlight = []
    for x in map4:
        T = [int(x[0:x.find(" ")]), int(x[x.find(" "):x.find(" ", x.find(" ") + 1)]),
             int(x[x.find(" ", x.find(" ") + 1):])]
        waterlight.append(T)
    map4.close()
    map5 = open("lighttemperaturemap.txt", "r")
    lighttemperature = []
    for x in map5:
        T = [int(x[0:x.find(" ")]), int(x[x.find(" "):x.find(" ", x.find(" ") + 1)]),
             int(x[x.find(" ", x.find(" ") + 1):])]
        lighttemperature.append(T)
    map5.close()
    map6 = open("temperaturehumidity.txt", "r")
    temperaturehumidity = []
    for x in map6:
        T = [int(x[0:x.find(" ")]), int(x[x.find(" "):x.find(" ", x.find(" ") + 1)]),
             int(x[x.find(" ", x.find(" ") + 1):])]
        temperaturehumidity.append(T)
    map6.close()
    map7 = open("humititylocationmap.txt", "r")
    humiditylocation = []
    for x in map7:
        T = [int(x[0:x.find(" ")]), int(x[x.find(" "):x.find(" ", x.find(" ") + 1)]),
             int(x[x.find(" ", x.find(" ") + 1):])]
        humiditylocation.append(T)
    map7.close()

    print("file reading done")

    seedsoilmap = customdik()
    for x in seedsoil:
        seedsoilmap.add(tuple((x[1],x[1]+x[2])),x[0])
    print("map 1 done")
    soilfretilizermap = customdik()
    for x in soilfretilizer:
        soilfretilizermap.add(tuple((x[1],x[1]+x[2])),x[0])
    print("map 2 done")
    fretilizerwatermap = customdik()
    for x in fretilizerwater:
        fretilizerwatermap.add(tuple((x[1],x[1]+x[2])),x[0])
    print("map 3 done")
    waterlightmap = customdik()
    for x in waterlight:
        waterlightmap.add(tuple((x[1],x[1]+x[2])),x[0])
    print("map 4 done")
    lighttemperaturemap = customdik()
    for x in lighttemperature:
        lighttemperaturemap.add(tuple((x[1],x[1]+x[2])),x[0])
    print("map 4 done")
    temperaturehumiditymap = customdik()
    for x in temperaturehumidity:
        temperaturehumiditymap.add(tuple((x[1],x[1]+x[2])),x[0])
    print("map 5 done")
    humiditylocationmap = customdik()
    for x in humiditylocation:
        humiditylocationmap.add(tuple((x[1],x[1]+x[2])),x[0])
    print("mapping done")

    minlocation=100000000000000000000000

    seedsoilmap.sorter()
    soilfretilizermap.sorter()
    fretilizerwatermap.sorter()
    waterlightmap.sorter()
    lighttemperaturemap.sorter()
    temperaturehumiditymap.sorter()
    humiditylocationmap.sorter()


    for i in seeds:
        S=seedsoilmap.getranges(tuple((i[0],i[0]+i[1])))
        for s in S:
            F=seedsoilmap.getranges(s)
            for f in F:
                W=fretilizerwatermap.getranges(f)
                for w in W:
                    L=waterlightmap.getranges(w)
                    for l in L:
                        T=lighttemperaturemap.getranges(l)
                        for t in T:
                            H=temperaturehumiditymap.getranges(t)
                            for h in H:
                                L=humiditylocationmap.getranges(h)
                                L=sorted(L,key=lambda location: location[0])
                                minlocation=min(minlocation,L[0][0])
    print(minlocation)









#day1()
#day2()
#day3part1()
#day3part2()
#day4()
day5()


