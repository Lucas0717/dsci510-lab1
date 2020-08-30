#!/usr/bin/env python
# coding: utf-8

# In[53]:


print("Welcome to DSCI510!")


# In[54]:


print("You must be the legendary god that comes from the sky")


# In[2]:


x = 6
print(x)


# In[3]:


y = x * 7
print(y)


# In[4]:


name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, ()) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
    
print(bigword, bigcount)


# In[5]:


x = 43
x = x + 1
print(x)


# In[6]:


type('Hello, World! ')


# In[7]:


type(12)


# In[8]:


type(3.2)


# In[9]:


type('12')


# In[10]:


print(1 ,000 ,000)


# In[15]:


message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931

print(n)
print(pi)

type(message)


# In[16]:


print(1)
x = 2
print(x)


# In[17]:


minute = 59
minute/60


# In[18]:


minute = 59
minute//60


# In[19]:


1 + 1


# In[20]:


quotient = 7 // 3
print(quotient)

remainder = 7 % 3
print(remainder)


# In[21]:


first = 10
second = 15
print(first + second)


# In[22]:


first = '100'
second = '150'
print(first + second)


# In[24]:


first = 'Test '
second = 3
print(first * second)


# In[25]:


inp = input()
print(inp)


# In[27]:


name = input('What is your name?\n')
print(name)


# In[29]:


a = 35.0
b = 12.50
c = a * b
print(c)


# In[30]:


hour = 35.0
rate = 12.50
pay = hour * rate
print(pay)


# In[31]:


1.0 / 2.0 * pi


# In[33]:


Name = input('Enter your name: ')
print('Hello ' + Name)


# In[35]:


width = 17
height = 12.0
width//2


# In[36]:


width/2.0


# In[37]:


height/3


# In[38]:


5 == 5


# In[39]:


5 == 6


# In[40]:


type(True)


# In[41]:


x =3
if x < 10 :
    print('Small')


# In[42]:


x = 3
if x < 10 :
    print('Small')
print('Done')


# In[43]:


x = 5
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')


# In[46]:


x = 4
y = 5
if x < y :
    print('x is less than y')
elif x > y :
    print('x is greater than y')
else:
    print('x and y are equal')
    


# In[47]:


x = 7
if 0 < x :
    if x < 10 :
        print('x is a positive single-digit number. ')


# In[48]:


inp = input('Enter Faharenheit Temperature: ')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)


# In[49]:


x = 6
y = 2
x >= 2 and (x/y) > 2


# In[50]:


x = 1
y = 0
x >= 2 and (x/y) >2


# In[52]:


inp = input('Enter a score(0.0 - 1.0): ')
x = float(inp)
if x >= 0.9:
    print('A')
elif x >= 0.8:
    print('B')
elif x >= 0.7:
    print('C')
elif x >= 0.6:
    print('D')
else:
    print('F')


# In[ ]:




