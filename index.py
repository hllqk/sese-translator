import pypinyin
import json
def py(list):
    se=''
    for i in list:
           file=open('txt.txt','a+')
           sese=hp(i)
           se+=sese+','
    file.write(se)
    file.seek(0)
    txt=file.read()
    file.close()
    #print(txt)
def hp(word):
    first= ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        to=''.join(i)
        first+=to[0]
    return first
sese=open('sese.txt','r')
list=json.load(sese)
#r=py(list)
strr=input('please write:')
#strr=str(strr)
for i in list:
   if hp(i)==strr:
       print(i)
       quit()
print('not found')