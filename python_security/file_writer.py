import hashlib
class read():
    def readlist(self,wordlist):
        OR=open(wordlist,"r")
        return OR.readlines()

r=read()
#من أجل قراءة المحتوى في الملف
alltext=r.readlist("text.txt")
for text in alltext:
    #إزالة السطور الفارغة
    text=text.rstrip("\n")
    text=text.encode("utf-8")
    h=hashlib.new("md5")
    h.update(text)
    hv=h.hexdigest()
    print(hv)