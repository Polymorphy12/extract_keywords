import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

# Data Preprocessing
def preprocessing(text):
    outputPath = "C:/Users/ty79450/Desktop/2019Dev/2019_toy_projects/extract_keywords_from_paper/preprocessed/"

    fileOut = open(outputPath + '1-s2.0-S1877050915036182-main' + '.csv', 'w', encoding='utf-8')
    
    # tokenize into words
    tokens = [word for sent in nltk.sent_tokenize(text)
              for word in nltk.word_tokenize(sent)]

    print( "- tokenize into words -" )
    print( tokens )
    print (tokens, file=fileOut)
    print()
    
    # remove stopwords
    stop = stopwords.words('english')
    tokens = [token for token in tokens if token not in stop]

    print( "- remove stopwords -" )
    print( tokens )
    print (tokens, file=fileOut)
    print()
    
    # remove words less than three letters
    tokens = [word for word in tokens if len(word) >= 3]

    print( "- remove words less than three letters -" )
    print( tokens )
    print (tokens, file=fileOut)
    print()
    
    # lower capitalization
    tokens = [word.lower() for word in tokens]

    print( "- lower capitalization -" )
    print( tokens )
    print (tokens, file=fileOut)
    print()
    
    # lemmatization
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(word) for word in tokens]

    print( "- lemmatization -" )
    print( tokens )
    print (tokens, file=fileOut)
    print()

    tokens = [lmtzr.lemmatize(word, 'v') for word in tokens]

    print( "- lemmatization/verb -" )
    print( tokens )
    print (tokens, file=fileOut)
    print()

    fileOut.close()

    # stemming
    #stemmer = PorterStemmer()
    #tokens = [ stemmer.stem(word) for word in tokens ]

    #print( "- stemming -" )
    #print(tokens)
    #print()
    
    preprocessed_text= ' '.join(tokens)
    return nltk.FreqDist(tokens)

#data = "The meaning is well known, even if it is not in complete accord with the reality. The restored stream evokes the environment but is not environmental, evokes history but is not historical, and evokes tradition without being traditional. The reality is conflicted. The restoration was huge in scale and high in cost. The cost overruns alone amounted to $34 million out of a total of about $351 million. Annual maintenance costs have been increasing while the overall number of visitors has declined."


with open('./full_text/1-s2.0-S1877050915036182-main.txt', 'r', encoding='UTF8') as file:
    data = file.read().replace('\n', ' ')

preprocessed = preprocessing(data)

print(preprocessed)

preprocessed.plot(100, cumulative=False)

##outputPath = "C:/Users/ty79450/Desktop/2019Dev/2019_toy_projects/extract_keywords_from_paper/preprocessed/"
##
##
##fileOut = open(outputPath + 'rafiki' + '.csv', 'w', encoding='utf-8')
##print (preprocessed, file=fileOut)
##fileOut.close()
