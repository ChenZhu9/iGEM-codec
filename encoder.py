import binascii
import re
import os
import datetime
from PIL import Image
from encode import *
MAXX = 12;
MAXY = 8;
#msg_in = [ 0x40, 0xd2, 0x75, 0x47, 0x76, 0x17, 0x32, 0x06,0x27, 0x26, 0x96, 0xc6, 0xc6, 0x96, 0x70, 0xec ]
#msg = rs_encode_msg(msg_in, 10)

def encode_2(s):
    tmp = []
    for c in s:
        tmpstr=bin(ord(c)).replace('0b', '')
        strasc=tmpstr.zfill(8)
        tmp.append(strasc)
    str_bin = ' '.join(tmp)
    return (str_bin)


def putsquare(a,b,c):
    for i in range(a,a+9):
      for j in range(b,b+9):
          pic.putpixel([i,j],c)
        
def draw(str):
    i=0
    for y in range (0,MAXY*10,10):
        if(i>=len(str)):
                break
        for x in range (0,MAXX*10,10):
            if(i>=len(str)):
                break
            if(str[i] == '1'):
                putsquare(x,y,(127,255,0))
            elif(str[i] == '0'):
                putsquare(x,y,(255,255,255))
            else:
                x=x-10
            i = i+1
    
data = input("Please input the stored data:")
str1=encode_2(data)
#str1=str1+"0"
msg = rs_encode_msg([ord(x) for x in data], 4)
tmp2 = []

def cut_text(text,lenth): 
     textArr = re.findall('.{'+str(lenth)+'}', text) 
     textArr.append(text[(len(textArr)*lenth):]) 
     return textArr 
    
for c in msg:
    tmpmsg=bin(c).replace('0b', '')
    strmsg=tmpmsg.zfill(8)
    tmp2.append(strmsg)
    str0 =''.join(tmp2)
file = os.getcwd() 
if os.path.exists(file+"\\mircoplate")==0:
    os.mkdir(file+"\\mircoplate") #Save pic to son directory "mircoplate"
list1=cut_text(str0,96)
num=1
timenow=datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
for s in list1:
    pic = Image.new("RGB",(10*MAXX,10*MAXY))
    draw(s)
    pic.save(file+"\\mircoplate\\"+timenow+"_"+str(num)+".jpg","JPEG")
    num=num+1
    
print("Please check the image in the directory",file+"\\mircoplate")
