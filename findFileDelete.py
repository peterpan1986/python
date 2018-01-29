#!python3
# findFileDelete.py
#搜索指定目录下大于100M的文件，打印出来并删除
#可以手动创建一个指定大小的空文件做试验
#dd if=/dev/zero of=hello.txt bs=100M count=1
dst='/root/test/'
for foldname,subfolders,filenames in os.walk(dst):
    for files in filenames:
        if os.path.getsize(dst+files)/1024/1024>100:
            print('大于100M的文件有:' + files +' '+ str(os.path.getsize(dst + files)/1024/1024)+'Mb')
            send2trash.send2trash(dst+ files)
