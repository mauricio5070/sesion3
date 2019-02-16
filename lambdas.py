#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Funcion anonima
#Lambda


# In[2]:


#suma


# In[12]:


a=lambda x,y: (x+y)


# In[10]:


c= lambda x,y : (x**2+ y**2)**0.5 


# In[11]:


c(3,2)


# In[13]:


a(5,1)


# In[14]:


imprimir_lowers= lambda x : print(x.lower())


# In[15]:


imprimir_lowers('Hola A TODOS LOS PRESEntES')


# In[16]:


imprimir_uppers= lambda x : print(x.upper())


# In[17]:


imprimir_uppers('Hola a todos')


# ## MAP

# In[18]:


l=[1,2,3,4,5,6,7,8,9]


# In[20]:


list(map( lambda x: x**2 +2*x +2,l))


# In[21]:


list(map(str,l))


# In[22]:


# filter


# In[24]:


list(filter(lambda x:x>4,l))


# In[25]:


#reduce


# In[29]:


l=[1,2,3,4]


# In[30]:


from functools import reduce 


# In[31]:


reduce(lambda x,y : x+y,l)


# In[32]:


## list comprehension 


# In[34]:


[i*2 for i in l]


# In[36]:


[print(i) for i in l if i<3]


# In[ ]:




