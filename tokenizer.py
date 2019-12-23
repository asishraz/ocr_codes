#simple program of tokenization 

#importing nltk library
import nltk
text = "this is Asish's text, isn't it? "


'''these all are first step of tokenization 
1. white space tokenization
'''
tokenizer1 = nltk.tokenize.WhitespaceTokenizer()
whitespace_text = tokenizer1.tokenize(text)
print("white space tokenization: ")
print(whitespace_text)
print()

'''
2. punctuation tokenization
'''
tokenizer2 = nltk.tokenize.WordPunctTokenizer()
punctuation_text = tokenizer2.tokenize(text)
print("punctuation tokenization: ")
print(punctuation_text)
print()

'''
3. grammar tokenization
'''

tokenizer3 = nltk.tokenize.TreebankWordTokenizer()
grammar_text = tokenizer3.tokenize(text)
print("grammar tokenization: ")
print(grammar_text)
print()

