#-*-encoding:utf-8
from tika import parser
import os
import shutil

'''
샘플 주석을 작성하겠습니다.
'''
dirPath = "C:/Users/ty79450/Desktop/2019Dev/2019_toy_projects/extract_keywords_from_paper/papers/"
outputPath = "C:/Users/ty79450/Desktop/2019Dev/2019_toy_projects/extract_keywords_from_paper/full_text/"
pdfInPath = os.listdir("C:/Users/ty79450/Desktop/2019Dev/2019_toy_projects/extract_keywords_from_paper/papers")
processedFileGoesTo = "C:/Users/ty79450/Desktop/2019Dev/2019_toy_projects/extract_keywords_from_paper/papers_processed/"

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
