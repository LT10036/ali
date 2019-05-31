# import xlrd
# import xlwt
#
# tb=xlrd.open_workbook("C:\\Users\\Administrator\\Desktop\\cs.xls")
# #
#
# # 计数当前  xls 文件里面有几张表格
# count=len(tb.sheets())
# # print(count)
#
#
# # 获取所有子表格的名字
# sheets = tb.sheet_names()
#
# for name in sheets:
#     print(name)
#
# # 打开指定表格，用表明来指定
# work_s = tb.sheet_by_name("日志")
#
# # 第一行
# rows = work_s.row_values(0)
#
# # 第一列
# cols = work_s.col_values(0)
# print(rows)
# print(cols)
#
#
# # 输出指定单元格数据  左上角为（0,0）
# print(work_s.cell(3,0))
#
# # 指定的表格有多少行
# print(work_s.nrows)
#
# # 指定的表格有多少列
# print(work_s.ncols)


#
# import xlwt
#
# wbk = xlwt.Workbook()
#
# sheet = wbk.add_sheet('写入')
#
# sheet.write(0,1,'222')#第0行第一列写入内容
#
# wbk.save("cs.xls")




f=open("hc.txt","r",encoding="utf-8")

m=f.readline()
while True:
    line = f.readline()
    if not line:
        f.close()
        break

    else:
        for i in line:
            if i[0]=="：":
                print(line)
            else:
                continue





