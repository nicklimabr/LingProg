#!/usr/bin/env python
# coding: utf-8

# In[10]:


peso = float (input("Digite o peso do peixe:"))


# In[6]:


taxa = 4


# In[11]:


if(peso>50):
    print(" A taxa é de:", taxa*(peso - 50), "R$")
else:
    print("Não há taxa adicional")

