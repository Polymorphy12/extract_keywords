#-*-encoding:utf-8
from tika import parser
import os
import shutil

'''
주석을 다시 만들었습니다.
'''
dirPath = "./papers/"
outputPath = "./full_text/"
pdfInPath = os.listdir("./papers")
processedFileGoesTo = "./papers_processed/"

for pdfFile in pdfInPath:
    print(pdfFile)

for pdfFile in pdfInPath:
    print("텍스트 파일은 다음 폴더에 저장됩니다.")
    print("2019Dev\2019_toy_projects\extract_keywords_from_paper\full_text")
    inputPath = dirPath + pdfFile

    
    
    parsed = parser.from_file(inputPath)
    outputFileName = pdfFile.split('.pdf')[0] + '.txt'
    fileOut = open(outputPath + outputFileName, 'w', encoding='utf-8')
    print(parsed['content'], file=fileOut)
    fileOut.close()

    shutil.move(inputPath, processedFileGoesTo + pdfFile)
##print("텍스트 파일을 추출할 PDF 파일명을 입력하세요.")
##PDFfileName = input()
##
##print("텍스트 파일은 다음 폴더에 저장됩니다.")
##print("D:\2019_toy_projects\extract_keywords_from_paper\full_text")
##inputPath = PDFfileName
##
##parsed=parser.from_file(PDFfileName)
##fileOut=open('fileOut.txt', 'w', encoding='utf-8')
##print(parsed['content'], file=fileOut)
##fileOut.close()
