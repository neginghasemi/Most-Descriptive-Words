from sklearn.feature_extraction.text import CountVectorizer
import time
import math
import codecs

collCount = []
collFeatures = []
collSumWords = []
wordCollIndex = -1
wordCollCount = -1

docCount = []
docFeatures = []
docSumWords = []
wordDocIndex = -1
wordDocCount = -1

collCountBigram = []
collFeaturesBigram = []
collSumWordsBigram = []
wordCollIndexBigram = -1
wordCollCountBigram = -1

docCountBigram = []
docFeaturesBigram = []
docSumWordsBigram = []
wordDocIndexBigram = -1
wordDocCountBigram = -1

def CollectionCounter(collPath) :
    with open(collPath, 'r') as fileCollection:
        collection = fileCollection.read().replace('\n', '')
    fileCollection.close()
    collection = [collection]
    vectorizer = CountVectorizer(ngram_range=(1, 1), token_pattern=r'\b\w+\b', min_df=0)
    global collCount, collFeatures, collSumWords
    collCount = vectorizer.fit_transform(collection).toarray()
    collFeatures = vectorizer.get_feature_names()
    collSumWords = [sum(row) for row in collCount]
    print(collSumWords)

def WordCollCounter(word):
    global wordCollIndex, wordCollCount
    try:
        wordCollIndex = collFeatures.index(word)
    except ValueError:
        wordCollIndex = -1
    if wordCollIndex != -1:
        wordCollCount = collCount[0][wordCollIndex]
    else:
        wordCollCount = 0

def DocCounter(docPath) :
    with open(docPath, 'r') as fileDocument:
        document = fileDocument.read().replace('\n', '')
    fileDocument.close()
    document = [document]
    vectorizer = CountVectorizer(ngram_range=(1, 1), token_pattern=r'\b\w+\b', min_df=0)
    global docCount, docFeatures, docSumWords
    docCount = vectorizer.fit_transform(document).toarray()
    docFeatures = vectorizer.get_feature_names()
    docSumWords = [sum(row) for row in docCount]
    print(docSumWords)

def WordDocCounter(word):
    global wordDocIndex, wordDocCount
    try:
        wordDocIndex = docFeatures.index(word)
    except ValueError:
        wordDocIndex = -1
    if wordDocIndex != -1:
        wordDocCount = docCount[0][wordDocIndex]
    else:
        wordDocCount = 0

def CollectionCounterBigram(collPath) :
    with open(collPath, 'r') as fileCollection:
        collection = fileCollection.read().replace('\n', '')
    fileCollection.close()
    collection = [collection]
    vectorizer = CountVectorizer(ngram_range=(2, 2), token_pattern=r'\b\w+\b', min_df=1)
    global collCountBigram, collFeaturesBigram, collSumWordsBigram
    collCountBigram = vectorizer.fit_transform(collection).toarray()
    collFeaturesBigram = vectorizer.get_feature_names()
    collSumWordsBigram = [sum(row) for row in collCountBigram]
    print(len(collFeaturesBigram))
    print(collSumWordsBigram)

def WordCollCounterBigram(word):
    global wordCollIndexBigram, wordCollCountBigram
    try:
        wordCollIndexBigram = collFeaturesBigram.index(word)
    except ValueError:
        wordCollIndexBigram = -1
    if wordCollIndexBigram != -1:
        wordCollCountBigram = collCountBigram[0][wordCollIndexBigram]
    else:
        wordCollCountBigram = 0

def DocCounterBigram(docPath) :
    with open(docPath, 'r') as fileDocument:
        document = fileDocument.read().replace('\n', '')
    fileDocument.close()
    document = [document]
    vectorizer = CountVectorizer(ngram_range=(2, 2), token_pattern=r'\b\w+\b', min_df=1)
    global docCountBigram, docFeaturesBigram, docSumWordsBigram
    docCountBigram = vectorizer.fit_transform(document).toarray()
    docFeaturesBigram = vectorizer.get_feature_names()
    docSumWordsBigram = [sum(row) for row in docCountBigram]
    print(docSumWordsBigram)

def WordDocCounterBigram(word):
    global wordDocIndexBigram, wordDocCountBigram
    try:
        wordDocIndexBigram = docFeaturesBigram.index(word)
    except ValueError:
        wordDocIndexBigram = -1
    if wordDocIndexBigram != -1:
        wordDocCountBigram = docCountBigram[0][wordDocIndexBigram]
    else:
        wordDocCountBigram = 0

if __name__ == '__main__':
    start_time = time.time()
    result_1 = open('result_1.txt', 'w')
    landa1 = 0.01
    landa2 = 0.1
    landa3 = 0.3
    landa4 = 0.5
    miu = 0.2

    # Unigram's Calculation
    CollectionCounter("/Users/negin/Desktop/HAM2-corpus-all.txt")
    DocCounter("/Users/negin/Desktop/input3.txt")
    print("Unigram's Collection is Finished")
    P1 = []
    P2 = []
    P3 = []
    P4 = []
    for i in range(0, len(docFeatures)):
        WordCollCounter(docFeatures[i])
        WordDocCounter(docFeatures[i])

        PWi1 = math.pow(10, wordDocCount * math.log10(landa1 * (wordDocCount / docSumWords[0]) + (1 - landa1) * (wordCollCount / collSumWords[0])))
        PWi2 = math.pow(10, wordDocCount * math.log10(landa2 * (wordDocCount / docSumWords[0]) + (1 - landa2) * (wordCollCount / collSumWords[0])))
        PWi3 = math.pow(10, wordDocCount * math.log10(landa3 * (wordDocCount / docSumWords[0]) + (1 - landa3) * (wordCollCount / collSumWords[0])))
        PWi4 = math.pow(10, wordDocCount * math.log10(landa4 * (wordDocCount / docSumWords[0]) + (1 - landa4) * (wordCollCount / collSumWords[0])))
        P1.append((docFeatures[i], PWi1))
        P2.append((docFeatures[i], PWi2))
        P3.append((docFeatures[i], PWi3))
        P4.append((docFeatures[i], PWi4))

    print("Writing Unigram.csv")
    columnTitleRow = "landa = 0.01, landa = 0.1, landa = 0.3, landa = 0.5\n"
    unigram = codecs.open("/Users/negin/Desktop/Unigram_3.csv", "wb", "utf-8")
    unigram.write(columnTitleRow)
    temp1 = sorted(P1, key=lambda p1: p1[1])[:10]
    temp2 = sorted(P2, key=lambda p2: p2[1])[:10]
    temp3 = sorted(P3, key=lambda p3: p3[1])[:10]
    temp4 = sorted(P4, key=lambda p4: p4[1])[:10]
    for i in range(0, 10):
        line = temp1[i][0]
        line += ', '
        line += temp2[i][0]
        line += ', '
        line += temp3[i][0]
        line += ', '
        line += temp4[i][0]
        line += '\n'
        unigram.write(line)
    unigram.close()
    print("Unigram is Finished")

    # Bigram's Calculation
    CollectionCounterBigram("/Users/negin/Desktop/HAM2-corpus-all.txt")
    DocCounterBigram("/Users/negin/Desktop/input3.txt")
    print("Bigram's Collection is Finished")
    landa5 = miu / (docSumWords[0] + miu)
    PB1 = []
    PB2 = []
    PB3 = []
    PB4 = []
    for i in range(0, len(docFeaturesBigram)):
        WordCollCounterBigram(docFeaturesBigram[i])
        WordDocCounterBigram(docFeaturesBigram[i])
        WordDocCounter(docFeaturesBigram[i].split(' ')[0])
        TF = wordDocCount
        WordDocCounter(docFeaturesBigram[i].split(' ')[1])

        PBWi1 = math.pow(10, wordDocCountBigram * math.log10(landa1 * (landa5 * (wordDocCountBigram / TF) + (1 - landa5) * (wordDocCount / docSumWords[0])) + (1 - landa1) * (wordCollCountBigram / collSumWordsBigram[0])))
        PBWi2 = math.pow(10, wordDocCountBigram * math.log10(landa2 * (landa5 * (wordDocCountBigram / TF) + (1 - landa5) * (wordDocCount / docSumWords[0])) + (1 - landa2) * (wordCollCountBigram / collSumWordsBigram[0])))
        PBWi3 = math.pow(10, wordDocCountBigram * math.log10(landa3 * (landa5 * (wordDocCountBigram / TF) + (1 - landa5) * (wordDocCount / docSumWords[0])) + (1 - landa3) * (wordCollCountBigram / collSumWordsBigram[0])))
        PBWi4 = math.pow(10, wordDocCountBigram * math.log10(landa4 * (landa5 * (wordDocCountBigram / TF) + (1 - landa5) * (wordDocCount / docSumWords[0])) + (1 - landa4) * (wordCollCountBigram / collSumWordsBigram[0])))
        PB1.append((docFeaturesBigram[i], PBWi1))
        PB2.append((docFeaturesBigram[i], PBWi2))
        PB3.append((docFeaturesBigram[i], PBWi3))
        PB4.append((docFeaturesBigram[i], PBWi4))
    print("Writing Bigram.csv")
    columnTitleRow = "landa = 0.01, landa = 0.1, landa = 0.3, landa = 0.5\n"
    bigram = codecs.open("/Users/negin/Desktop/Bigram_3.csv", "wb", "utf-8")
    bigram.write(columnTitleRow)
    temp1 = sorted(PB1, key=lambda pb1: pb1[1])[:10]
    temp2 = sorted(PB2, key=lambda pb2: pb2[1])[:10]
    temp3 = sorted(PB3, key=lambda pb3: pb3[1])[:10]
    temp4 = sorted(PB4, key=lambda pb4: pb4[1])[:10]
    for i in range(0, 10):
        line = temp1[i][0]
        line += ', '
        line += temp2[i][0]
        line += ', '
        line += temp3[i][0]
        line += ', '
        line += temp4[i][0]
        line += '\n'
        bigram.write(line)
    bigram.close()
    print("Bigram is Finished")