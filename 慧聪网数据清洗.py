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

    while True:

        m=f.readline()
        if "手机号" in m:
            row+=1
            break
        else:
            if not m:
                f.close()
                s=0
                tb.save("慧聪网商家02.xls")

                break
            else:

                if m[0] == "：":
                    st.write(row, lin, m[1:])
                    lin+=1
                else:
                    continue

    lin = 0













