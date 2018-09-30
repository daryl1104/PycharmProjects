import os,os.path,time

def FileSplit(sourceFile,targetFolder):
    sFile=open(sourceFile,'r')
    tempdata=[]
    number=100000
    dataline=sFile.readline()
    fileNum=1
    if not os.path.isdir(targetFolder):
        os.mkdir(targetFolder)
    while dataline:
        for i in range(number):
            tempdata.append(dataline)
            dataline=sFile.readline()
            if not dataline:
                break
        tFileName=os.path.join(targetFolder,str(sourceFile)+str(fileNum)+".txt")
        tFile=open(tFileName,'a+')
        tFile.writelines(tempdata)
        tempdata=[]
        fileNum+=1

    sFile.close()

if __name__=="__main__":
    FileSplit("access.log","/tmp")