#! python3
# coding:utf-8

import re,os

fdir='/root/python/py-9/test/'
fdir_list=os.listdir(fdir)
fdir_count=len(fdir_list)

print(fdir_list)
print('该目录下共有%d个文件' % fdir_count)

f_pre='spam'
f_num=[]
f_end='.txt'
fs_list=[]

#这里只假定文件数量小于100的情况
for i in range(1,fdir_count+1):
    if i<10:
        f_name=f_pre+'00'+str(i)+f_end
        f_num.append('00'+str(i))
        fs_list.append(f_name)
    else:
        f_name=f_pre+'0'+str(i)+f_end
        f_num.append('0'+str(i))
        fs_list.append(f_name)

max_f_num=max(f_num)
print('该目录下文件最大的编号应该是: %s' %max_f_num)
print('正确的文件名应该是:')
print(fs_list)

#使用正则表达式搜索目录中已有编号的文件并存入列表yf_num中
re_num='\d{3}'
yf_num=re.findall(f_pre + re_num +f_end,' '.join(fdir_list))
ra_num=re.findall(re_num,' '.join(fdir_list))
print('目录中已有编号文件: \n%s' % yf_num)

#fq_list为目录中缺失编号的文件名列表
#fx_list为当前目录中需要修改名称的文件列表

fq_list = []
fx_list = []

#定位缺失的编号文件并放入列表中
for a in fs_list:
    if a not in yf_num:
        fq_list.append(a)
print('缺少的文件编号是: \n%s' % fq_list)

#查找目录中没有编号或不正连续的编号文件并放入列表中
for f_rename in fdir_list:
    if f_rename not in fs_list:
        fx_list.append(f_rename)
print('需要修改的文件名有:\n%s' % fx_list)


#更改文件名
for k in fq_list:
    for v in fx_list:
        os.rename(fdir+v,fdir+k)
        #每当修完一个文件名应该更新一下这个列表
        fx_list.remove(v)
print('改完名后的结果为:')
os.system('ls')

