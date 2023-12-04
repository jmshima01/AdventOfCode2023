
digs = ['1','2','3','4','5','6','7','8','9','0']
words = 'onetwothreefourfivesixseveneightninezero'
rev = [i[::-1] for i in words]
d = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}

def subset(s):
    for i in range(len(s)):
        temp = ""
        for j in range(i,len(s)):
            temp+=s[j]
            if(temp in d.keys()):
                return str(d[temp])
    return None



def getFirst(s):
    temp = ""
    for i in s:
        temp+=i
        if i in digs:
            return i
        if subset(temp) != None:
            return subset(temp)
        if subset(temp[::-1])!=None:
            return str(subset(temp[::-1]))

with open("day1.txt","r+") as f:
    l = f.read().split("\n")
    f = []
    for i in l:
        lef = getFirst(i)
        rig = getFirst(i[::-1])
        res = lef+rig
        print(i,res)
        f.append(int(res))

print(sum(f))
 