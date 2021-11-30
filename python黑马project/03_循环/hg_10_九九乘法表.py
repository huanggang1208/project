# 打印九行小星星
# 定义一个行的变量 cow
row = 1

while row <= 9:

    col = 1

    while col <= row:

        # 定义一个结果变量 fam
        fam = col * row

        # 增加一个转义字符 \t ，使得列对齐
        print("%d*%d=%d"% (col,row,fam),end="\t")

        col += 1

    print("")

    row += 1