import os

def split(sourceFile):
    file=open(sourceFile, 'r')
    list1=[]
    num=1000
    i=0
    content=file.read(1024)
    fileNum=1
    while content:
        for i in range(num):
            list1.extend(content)
            content=file.read(1024)
            if not content:
                break
        tFileName=os.path.join(str(sourceFile)+str(fileNum)+".txt")
        ofile=open(tFileName,'a+')
        ofile.write(content)
        list1=[]
        fileNum+=1

if __name__=='__main__':
    split("/wiki_seg.txt")