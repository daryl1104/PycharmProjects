import os
import logging
from gensim.models import word2vec

def checkTxtFile(FilePath):
    dirPath=[]
    for dir in os.listdir(FilePath):
        childDir = os.path.join(FilePath, dir)
        if os.path.isdir(childDir):
            checkTxtFile(childDir)
        else:
            if childDir[-4]=='.txt':
                dirPath.append(childDir)
    return dirPath

def initTrainWord2VecModel(self,corpusFilePath):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    fileList=checkTxtFile(corpusFilePath)
    model=Word2Vec(sentences,size=350,sg=1,min_count=100,iter=5)
    for file in fileList[1:len(fileList)]:
        model=updateW2VModelUnit(model,file)
    model.save("word2vec.model")

def updateW2VModelUnit(self,model,file):
    with open(file,'r')as corpusFile:
        trainedWordCount=model.train(LineSentence(corpusFile))
        print('update model, update words num is: ' + trainedWordCount)
    return model

if __name__=='__main__':
    initTrainWord2VecModel("/home/gensim/")