#simple program of tokenization 

#importing nltk library
import nltk
text = "this is Asish's text, isn't it? "

tokenizer = nltk.tokenize.WhitespaceTokenizer()
whitespace_text = tokenizer.tokenize(text)
print(whitespace_text)