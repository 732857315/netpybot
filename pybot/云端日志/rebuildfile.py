
import os

f_dir = input('输入文件地址：')

f_in = open(f_dir,'r',encoding='UTF-8')
f_out = open('./file_remove.txt','w+',encoding='UTF-8')

oldline=''
linenum=1
writelinenum=0
while True:
    newline = f_in.readline(linenum)
    linenum=linenum+1
    if oldline == newline:
        continue
    if '127.0.0.1 - - [' in newline:
        if '] \"POST / HTTP/1.1\" 200 -' in newline:
            continue
    if newline =='':
        break
    oldline = newline
    f_out.write(newline)
    writelinenum=writelinenum+1
    
print('文件行数：'+str(linenum-1)+' 写入行数：'+ str(writelinenum)+' 写入文件地址：'+os.getcwd()+' 文件名：file_remove.txt')
f_in.close()
f_out.close()


