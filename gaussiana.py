
# coding: utf-8

# In[40]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

sigma=0.01
x=np.linspace(-200,200)
e=np.e
pi=np.pi




# $$f(x)= 1 / \sqrt[2]{2\pi \sigma^2 }e^-(x^2/2 \sigma^2)$$

# In[44]:

def f(x):
    return (1/np.sqrt(2*pi*sigma**2))*(e**-((x**2)/2*(sigma**2)))

plt.plot(x,f(x),'--',color='g')
plt.xlabel('Eje de X')
plt.title('Funcion Gaussiana')
plt.grid()


# In[ ]:




# In[ ]:




# In[ ]:



