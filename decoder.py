from decode import *
import xlrd
data = xlrd.open_workbook("data.xls")
table = data.sheets()[0]          #通过索引顺序获取
nrows = table.nrows  #获取该sheet中的有效行数
def Index():#Find the positon of data
    tmp1=[]
    tmp2=[]
    for i in range(nrows):
        if(table.cell_value(i,0)=='A'):
            if(int(table.cell_value(i,1))>=2):
                tmp1.append(i)#flouresence
            else:
                tmp2.append(i)#od
    return tmp1,tmp2

flourindex,odindex=Index()  
msg=[]
def read(n):
    sum0=0
    tmp=[]
    data=""
    lenbyte=0
    len0=odindex[n]-flourindex[n]
    for i in range (flourindex[n],flourindex[n]+8):
        for j in range(1,13):
            gfp=float(table.cell_value(i,j))/float(table.cell_value(i+len0,j))
            tmp.append(gfp)
            sum0=sum0+gfp
    avg=sum0/96
    for i in range (0,96):
        lenbyte=lenbyte+1
        if tmp[i]>=avg:
            tmp[i]=1
        else:
            tmp[i]=0
        data=data+str(tmp[i])
        if lenbyte==8:
            msg.append(int(data,2))
            data=""
            lenbyte=0
for i in range(0,len(odindex)):
    read(i)

nsym=4
synd = rs_calc_syndromes(msg, nsym)
err_loc = rs_find_error_locator(synd, nsym)
pos = rs_find_errors(err_loc[::-1], len(msg)) # find the errors locations
print("Error site:",pos)
msg = rs_correct_errata(msg, synd, pos)
for i in range (len(msg)-nsym):
    print(chr(msg[i]), end='')

