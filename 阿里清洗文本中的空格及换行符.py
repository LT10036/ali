
# 文本清洗空格和换行，保留下数字和汉字

f=open("ali03.txt","r",encoding="utf-8")
ln=open("阿里商家.txt","a",encoding="utf-8")


while True:
    line = f.readline()
    if not line:
        f.close()
        break

    else:
        m=line.split(" ")
        ne=[]
        for i in m:
            if i !="" :
                if i !="\n":
                    ne.append(i)
        l=str(ne)

        if len(l)>2:
            l="".join(ne)
            print(l)
            ln.write(l)
            ln.write("\n")

print("调取结束")
ln.close()






