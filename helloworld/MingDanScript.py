import os,os.path,time,random

def Generate1(sourceFile,targetFolder):
    sFile=open(sourceFile,'r')
    tempdata=[]
    number=10000
    dataline=sFile.readline()
    fileNum=1
    if not os.path.isdir(targetFolder):
        os.mkdir(targetFolder)
    while dataline:
        pass
        for i in range(number):
            cellphoneNum=dataline.split(",")
            strVar = str(i)+",ivr," + cellphoneNum[0] + ",M2_SIMPLE,CARDHOLD:朱丽娜|SEX:"+str(random.randint(1,2))+"|AC_TYP:1|CYCLE:25M\n"
            print(str(i)+": "+strVar)
            tempdata.append(strVar)
            dataline=sFile.readline()
            if not dataline:
                break
        tFileName=os.path.join(targetFolder,"M2_STMPLE"+".txt")   #F:\\M2_STMPLE.txt
        tFile=open(tFileName,'a+')
        tFile.writelines(tempdata)
        fileNum+=1
        dataline=sFile.readline()

    sFile.close()


def Generate2(sourceFile,targetFolder):
    sFile=open(sourceFile,'r')
    tempdata=[]
    number=10000
    dataline=sFile.readline()
    fileNum=1
    if not os.path.isdir(targetFolder):
        os.mkdir(targetFolder)
    while dataline:
        pass
        for i in range(number):
            cellphoneNum=dataline.split(",")
            strVar = str(i)+",ivr," + cellphoneNum[0] + ",M1_1ST,CARDHOLD:李四2|SEX:"+str(random.randint(1,2))+"|AC_TYP:1|CYCLE:25|STMT_BAL_R:14288|STMT_BAL_U:0|TOT_DUE_R:2521.72|TOT_DUE_U:0\n"
            print(str(i)+": "+strVar)
            tempdata.append(strVar)
            dataline=sFile.readline()
            if not dataline:
                break
        tFileName=os.path.join(targetFolder,"M1_1ST"+".txt")
        tFile=open(tFileName,'a+')
        tFile.writelines(tempdata)
        fileNum+=1
        dataline=sFile.readline()

    sFile.close()


def Generate3(sourceFile,targetFolder):
    sFile = open(sourceFile, 'r')
    tempdata = []
    number = 10000
    dataline = sFile.readline()
    fileNum = 1
    if not os.path.isdir(targetFolder):
        os.mkdir(targetFolder)
    while dataline:
        pass
        for i in range(number):
            cellphoneNum = dataline.split(",")
            strVar = str(i) + ",ivr," + cellphoneNum[0] + ",M1_2ND,CARDHOLD:李四3|SEX:"+str(random.randint(1,2))+"|AC_TYP:1|CYCLE:25|STMT_BAL_R:14288|STMT_BAL_U:0|TOT_DUE_R:2521.72|TOT_DUE_U:0\n"
            print(str(i) + ": " + strVar)
            tempdata.append(strVar)
            dataline = sFile.readline()
            if not dataline:
                break
        tFileName = os.path.join(targetFolder, "M1_2ND" + ".txt")
        tFile = open(tFileName, 'a+')
        tFile.writelines(tempdata)
        fileNum += 1
        dataline = sFile.readline()

    sFile.close()


if __name__=="__main__":
    Generate3("F:\\dataresult.txt","F:\\")