import os, shutil


def organizer(path=r""):
    
    os.listdir(path)

    folderNames=[]
    for p in os.listdir(path):
        if ' Files'  in p:
            folderNames.append(p)

    for p in os.listdir(path):
        if p[0]!='.':
            if (p[-3] =='.'):
                ext=p[-2:]+' Files'
            elif (p[-4] =='.'):
                ext=p[-3:]+' Files'
            elif (p[-5] =='.'):
                ext=p[-4:]+' Files'
            elif (p[-6] =='.'):
                ext=p[-5:]+' Files'
            else:
                continue
            if ext not in os.listdir(path):
                os.makedirs(path+'/'+ext)
            if ext not in folderNames:
                folderNames.append(ext)

    for file in os.listdir(path):
        if '.' in file:
            if (file[-3] =='.'):
                for folder in folderNames:
                    if file[-2:]==folder[:2]:
                        shutil.move(path+'/'+file,path+'/'+folder)
            elif (file[-4] =='.'):
                for folder in folderNames:
                    if file[-3:]==folder[:3]:
                        shutil.move(path+'/'+file,path+'/'+folder)
            elif (file[-5] =='.'):
                for folder in folderNames:
                    if file[-4:]==folder[:4]:
                        shutil.move(path+'/'+file,path+'/'+folder)
            elif (file[-6] =='.'):
                for folder in folderNames:
                    if file[-5:]==folder[:5]:
                        shutil.move(path+'/'+file,path+'/'+folder)
            else:
                print("The file "+file+" couldn't be moved")
