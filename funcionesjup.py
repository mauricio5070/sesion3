#!/usr/bin/env python
# coding: utf-8

# # Intro a las funciones en python

# In[1]:


print('Hola')


# # Práctica de funciones 

# ## Ejemplo de pitágoras 

# In[5]:


#importando la funcion ,atematica de la raiz cuadrada 
from math import sqrt


# In[6]:


def hipotenusa(cateto1,cateto2):
    return cateto1**2 + cateto2**2


# In[7]:


hipotenusa(2,3)


# In[ ]:


a='Lunes'; b='Martes';c='Sabado'


# In[17]:


q=5; w=5


# In[18]:


z=[q,w]


# In[19]:


hipotenusa(*z)


# In[20]:


a,b,c=['abaco','bola','cat']


# In[21]:


a


# In[22]:


b


# In[23]:


c


# In[24]:


l=('Dado','Queso','Frio')


# In[25]:


h,j,k=l


# In[26]:


h


# In[27]:


j


# In[28]:


k


# In[ ]:




