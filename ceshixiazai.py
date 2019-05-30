f = open ("111.txt","r",encoding='utf-8')

m=f.readline()
l=[]
for n in m:
    if n!=" ":
        l.append(n)
    else:
        continue
ln=str(l)
print(ln)