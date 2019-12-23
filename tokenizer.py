#simple program of tokenization 

#importing nltk library
import nltk
text = "this is Asish's text, isn't it? "


'''these all are first step of tokenization 
1. white space tokenization
'''
tokenizer = nltk.tokenize.WhitespaceTokenizer()
whitespace_text = tokenizer.tokenize(text)
print(whitespace_text)

'''
2. punctuation tokenization
'''
tokenizer = nltk.tokenize.WordPunctTokenizer()
punctuation_text = tokenizer.tokenize(text)
print(punctuation_text)

'''
3. grammar tokenization
'''

tokenizer = nltk.tokenize.TreebankWordTokenizer()
grammar_text = tokenizer.tokenize(text)
print(grammar_text)

