import os

document=raw_input()
#print document

path= os.path.abspath(os.curdir)+'\\test.txt'
#path_new=os.path.join('D:/eclipse','/test.txt')
print path
f=open(path,'w')
list1=document.split(' ')
list2 = list(set(list1))
list2.sort(key=list1.index)
print list2
for i in range(len(list2)):
    f.write(list2[i]+' ')
f.close()