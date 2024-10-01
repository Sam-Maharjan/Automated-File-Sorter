import os, shutil, random
'''Will create random files with extensions'''
path=r""'''<--Type path'''
os.listdir(path)
lst1=['.pdf','.xml','.jpeg','.docx','.png']
lst2=['.rtf','.txt','.py','.cpp','.json','.htf','.hf','.rft','.exe']
lst3=lst1+lst2

n=10
'''n=num of files'''
for i in range(n):
    open(path+"myfile"+str(i+random.randint(0, 1000)*random.randint(0, 100)*random.randint(0, 10))+random.choice(lst3), "w")