li=[1,2,3,"你好"]
print(len(li))
print(li[1])
print(type(li))
li.append("asd")
li.extend(["a",2,3])
li.insert(1,"脑浆")
print(li)
li[1]='Nya'
li.remove("你好")##移除指定的值
li.pop(1)##移除某位置的值
print(li)
print(li.index("a"))
li=[1,2,3]
li2=['a','s','d',li]
li.append(li2)
print(li2)