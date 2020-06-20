from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

tokenizer= RegexpTokenizer(r'\w+')
ps= PorterStemmer()
en_stopword= stopwords.words('english')

def documentStemmer(document):
    document= document.lower()
    document=document.replace('<br /><br />',"")
    tokens=tokenizer.tokenize(document)
    new_tokens= [token for token in tokens if token not in en_stopword]
    
    stem_tokens=[ps.stem(token) for token in new_tokens]
    cleaned_document=' '.join(stem_tokens)
    return cleaned_document


def genCleanedDocument(in_file,out_file):
    
    out= open(out_file,'w',encoding='utf8')
    with open(in_file) as f:
        reviews= f.readlines()
        
    for review in reviews:
        print(documentStemmer(review),file=out)
    
    out.close()
    
    