#! python3
# selectiveCopy.c

import os,shutil
os.chdir('old')
#to generate a file, and make sure the file has not existed
try:
    os.makedirs('copy_to_this_dir')
except FileExistsError:
    pass
for root,dirs,files in os.walk('.'):
    for file in files:
# what kind of file that you want to copy
        if file.endswith('.bak') or file.endswith('.dat'):
#这一步很重要，是为了排除自己复制成自己（因为os.walk的直线遍历性）
            if file not in os.listdir('copy_to_this_dir'):
#copy these files to a new folder
                    shutil.copy(os.path.jion(root,file),'copy_to_this_dir')
