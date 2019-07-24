#!/usr/bin/env python
# coding: utf-8

# # 第一次课作业

# ## （1）python基础语法。

# （1）下面两段代码输出的结果相同么？请解释原因。    
# ① x=4，y=5，print（x+y） 
# ② x='4',y='5', print(x+y)

# In[1]:


x=4
y=5 # x,y 为 int 类型
print(x+y) 


# In[2]:


x='4'
y='5' #x,y 为 str (字符串)
print(x+y)


# （2）‘10/3'，‘10//3’和'10%3'结果相同么？请说明原因。

# In[3]:


10/3 # 普通除法


# In[4]:


10//3 # 取整商


# In[5]:


10%3 # 取模


# （3）string1='I'm a student.' 。print(string1)结果会报错么？如何修改string1使其得到正确的输出？

# In[6]:


string1='I'm a student.'
print(string1)


# In[7]:


string1='I\'m a student.' # ' 单引号不能单独出现 要加\
print(string1)


# （4） a = 3，str(a\*3) + str(a)\*3的输出是什么?

# In[12]:


a = 3
str(a*3) + str(a)*3
# str(a*3) 等于9  str(a)*3为333


# （5）my_string = 'this is my string', 如何查看这个字符串长度？

# In[13]:


my_string = 'this is my string'
len(my_string)


# （6）a,b = 4,5,a大于b 或 b大于等于5。请写出这里逻辑运算的代码，并查看输出会是什么。

# In[15]:


a,b = 4,5
a>=b or b>=5   #or 为或 有一个true 输出true


# （7）'='和'=='分别表示什么含义？print(2==5)输出什么结果？属于什么类型数据？

# In[16]:


print(2==5) # ==判断


# （8）计算：100%(2+2)\*\*3//5

# In[17]:


100%(2+2)**3//5
100%4**3//5


# In[19]:


100%4**3//5


# In[21]:


100%64//5 #  同级


# In[22]:


100%64


# In[20]:


4**3


# In[18]:


2+2


# （9）a,b = 4,5，a \*= b，a=? 

# In[23]:


a,b = 4,5
a *= b #a=a*b


# （10）int(3.14159)==float(3)会输出什么结果？为什么？type(int(3.14159))==type(float(3))的结果又是什么？

# In[25]:


type(int(3.14159))==type(float(3)) # int 默认转换为 float  


# In[24]:


int(3.14159)


# ## （2）列表，字典，集合

# （1）L=[1,2,3,4,1,4,5,6],请完成：①删除列表中的重复元素并输出一个集合；②将7添加到集合中；③将集合转化为列表，删除元素3.

# In[2]:


L=[1,2,3,4,1,4,5,6] #列表
s=set(L) # 转换为集合
s


# In[4]:


s.add(7)
s


# In[9]:


l=list(s)
l


# In[10]:


l.pop(2)


# （2）dog = ["tom", "jack", "Collie", "Marry"], kitty = "Marry", 如何判断 kitty 是否是 dog 中的一员?

# In[11]:


dog = ["tom", "jack", "Collie", "Marry"]
kitty = "Marry"
kitty in dog


# （3）dog = ["tom", "jack", "Collie", "Marry"]，将dog逆序。

# In[12]:


dog [::-1] # 倒序


# In[13]:


dog [::2] #间隔为2


# （4）L=["former", "latter", "starboard"]，请完成：为L在末端添加一个元素“port”。

# In[14]:


L=["former", "latter", "starboard"]
L.append('port')
L


# （5）L=[1,2,3,1,5,11,3,6,4,2,5,8,4,2],计算L的最值，和加和。

# In[16]:


L=[1,2,3,1,5,11,3,6,4,2,5,8,4,2]


# In[17]:


max(L)


# In[18]:


min(L)


# In[19]:


sum(L)


# （6）cube：length：40，width：40，height：40, 请创建一个字典，包括cube的所有信息，并向字典中添加条目“color”和对应值"red"，  
# 删除属性height，修改属性width为20.

# In[34]:


cube={'length':40,'width':40,'height':40}
cube


# In[35]:


cube['color']='red'
cube


# In[36]:


cube.pop('height')


# （7）set_a = {1, 5, 10} set_b = {1, 10, 12} 找出set_a和set_b中共有的元素（交集）。

# In[39]:


set_a = {1, 5, 10}
set_b = {1, 10, 12}


# In[40]:


set_a & set_b


# In[41]:


set_a | set_b


# In[43]:


set_a - set_b


# （8）从1到10中选出所有的奇数。

# In[44]:


[1,2,3,4,5,6,7,8,9,10][::2]


# （9）将字典变为两个元素一一对应的列表，一个只含有关键字，另一个只含有值。 如:{'a': 1, 'b': 2}变为['a', 'b'], [1, 2]

# In[46]:


d={'a': 1, 'b': 2}


# In[47]:


d.values()


# In[48]:


d.keys()


# ## （3）条件判断，循环和函数

# （1）L=[1,2,'','my',3,'name','is',4,'katty'],利用循环语句和判断条件，分别输出列表中的字符串和数字。

# In[54]:


L=[1,2,'','my',3,'name','is',4,'katty']
str_list=[]
int_list=[]
for i in L:
    if type(i)==int:
        int_list.append(i)
    if type(i)==str:
        str_list.append(i)
    


# In[55]:


int_list


# In[56]:


str_list


# （2）利用循环语句输出1到50中5的倍数，将其存放到一个列表中。

# In[58]:


for i in range(1,51):
    if i % 5==0:
        print(i)


# （3）定义一个判断字符串的长度是否大于10的函数。

# In[61]:


def f(s):
    if len(s)>10:
        return True
    else:
        return False


# In[64]:


f('qeqeadad')


# （4）定义一个求解阶乘的函数。

# In[80]:


def f(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s


# In[76]:


f(6)


# （5）利用列表生成式，生成1-5的阶乘。

# In[82]:


[f(i) for i in range(1,6)]


# In[78]:


L=[f(i) for i in[1,2,3,4,5]]
L


# （6）利用函数和列表生成式，标记一个列表，奇数标记为1，偶数标记为2，并且统计一下奇数和偶数的数量。
#      例如：[1,4,2,4,2,9,5]，得到[1,2,2,2,2,1,1]

# In[85]:


def f(n):
    if type(n) !=int:
        print('wrong number')
        return 0
    if n%2 ==0:
        return 2
    else:
        return 1


# In[90]:


l=[f(i) for i in[1,4,2,4,2,9,5]]
l


# In[92]:


sum(l)-len(l)


# In[93]:


l.count(1)


# In[94]:


l.count(2)


# In[ ]:




