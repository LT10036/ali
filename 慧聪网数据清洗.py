import xlwt



# 打开excel，创建行0
tb = xlwt.Workbook()
st = tb.add_sheet("慧聪网",cell_overwrite_ok=True)

# 设置行列初始值为 0
row = 0
lin=0

# 打开文本需要转成
f = open("hc.txt","r",encoding="utf-8")

s=1

while s:

    for i in range(9):
        m=f.readline()
        if not m:
            f.close()
            s=0
            tb.save("慧聪网商家.xls")

            break
        else:

            if m[0] == "：":
                st.write(row, lin, m[1:])
                lin+=1
            else:
                continue
    row = row+1
    lin = 0













