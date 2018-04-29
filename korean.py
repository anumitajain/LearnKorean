# Korean speaking app
import codecs
f1 = codecs.open(file1, "r","utf-8")
text = f1.read()
print(type(text))
print(text.encode('utf-8'))


