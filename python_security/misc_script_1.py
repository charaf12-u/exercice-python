


import hashlib
class hashtext:
    def hashingtext(self,text,hash_type):
        text = text.encode("utf-8")
        h = hashlib.new(hash_type)
        h.update(text)
ht=hashtext()
hv=ht.hashingtext("hello","md5")
print(hv)