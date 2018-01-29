#! python3
# coding:utf-8
import re,os
fdir='/root/github/shell/python3/py-9/test/'
fdir_list=os.listdir(fdir)
fdir_f_count=len(fdir_list)
print('当前目录的文件为:\n %s' % fdir_list)
def getFileformat(f_pre,f_num,f_end):
    fileformat=f_pre+f_num+f_end
    return fileformat

file_list=[]
def getTruefile():
    for i in range(1,fdir_f_count+1):
        if i<10:
            f_format=getFileformat('spam','00'+str(1),'.txt')
            file_list.append(f_format)
        else:
            f_format=getFileformat('spam','0'+str(i),'.txt')
            file_list.append(f_format)
    return file_list
truefilelist=getTruefile()
print('正确的文件编号应该是:\n%s' % truefilelist)

lostnumfilelist=[]
def getLostnumfile(fdirlist,truelist):
    for lf in truelist:
        if lf not in fdirlist:
            lostnumfilelist.append(lf)
    return lostnumfilelist
lostnumfile=getLostnumfile(fdir_list,file_list)
print('缺失的文件编号为:\n%s' % lostnumfile)

renamelist=[]
def getrenamefile(fdirlist,func):
    for a in fdirlist:
        if a not in func:
            renamelist.append(a)
    return renamelist
renamefilelist=getrenamefile(fdir_list,file_list)
print('需要修改的文件是:\n%s' % renamefilelist)

def renamefile(func1,func2):
    for b in func1:
        for c in func2:
            os.rename(fdir+c,fdir+b)
            func2.remove(c)

rename= renamefile(lostnumfile,renamefilelist)
os.chdir(fdir)
print('修改后的结果为:')
os.system('ls')


         
