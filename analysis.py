import textblob
from textblob import TextBlob
import fileinput


def fileinput():
     with open("testfile.txt", "r") as file:
          sentence = file.read().replace('\n', '')
     wiki = TextBlob (sentence)
     val = wiki.sentiment
     print (val)
     
     return

fileinput()

