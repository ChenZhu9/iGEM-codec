from decode import *
import xlrd
data = xlrd.open_workbook("data.xls")
table = data.sheets()[1]          #通过索引顺序获取
nrows = table.nrows  #获取该sheet中的有效行数
def Index():#Find the positon of data
    tmp=[]
    j=0
    for i in range(nrows):
        if(table.cell_value(i,0)=='A'):
            tmp.append(i)
            j=j+1
    return tmp

index=Index()  
msg=[]
def read(n):
    sum0=0
    tmp=[]
    data=""
    lenbyte=0
    len0=index[n]-index[n-2]
    for i in range (index[n-2],index[n-2]+8):
        for j in range(1,13):
            gfp=float(table.cell_value(i,j))/float(table.cell_value(i+len0,j))
            tmp.append(gfp)
            sum0=sum0+gfp
    avg=sum0/96
    for i in range (0,96):
        lenbyte=lenbyte+1
        if tmp[i]>=avg:
            tmp[i]=0
        else:
            tmp[i]=1
        data=data+str(tmp[i])
        if lenbyte==8:
            msg.append(int(data,2))
            data=""
            lenbyte=0

read(2)
read(3)
print (msg)
nsym=4
synd = rs_calc_syndromes(msg, nsym)
err_loc = rs_find_error_locator(synd, nsym)
pos = rs_find_errors(err_loc[::-1], len(msg)) # find the errors locations
print(pos)
msg = rs_correct_errata(msg, synd, pos)
for i in range (len(msg)-nsym):
    print(chr(msg[i]), end='')
