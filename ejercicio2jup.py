#!/usr/bin/env python
# coding: utf-8

# # Ejercicio

# ## Se tiene una coleccion de datos 

# In[1]:


#('Carlos',2565644,'San Jose','carlos@gmail.com')


# In[2]:


#Crear una funcion que imprima el nombre, llame al numero de telefono,
#envie una carta a san jose y envie un correo electronico


# In[11]:


# La funcion se llama envia_datos


# In[14]:


info=('Carlos',22565644,'San Jose','carlos@gmail.com')


# In[15]:


def envia_datos(x):
    nombre,telefono,carta,email=x
    print('Nombre:',nombre)
    print('Llamando a:',telefono)
    print('Enviando carta a:',carta)
    print('Enviando correo a:',email)


# In[16]:


envia_datos(info)


# In[ ]:


input()


# In[ ]:




