import os
import shutil
srcpath = '/Users/User/Desktop/File/Projek menyelamatkan dunia/Face Images/Final Testing Images/face16'
despath = '/Users/User/Desktop/File/Projek menyelamatkan dunia/NEWMODEL/T'

files = os.listdir(srcpath)

shutil.copytree(srcpath, despath)

os.chdir(despath)
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "User.16." + str(count)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)