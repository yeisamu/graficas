
# coding: utf-8

# In[15]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5)
e=np.e


# $$f(x)=e^x-e^-x/e^x+e^-x$$

# In[ ]:

def f(x,e):
    return ((e**x)-(e**-x))/((e**x)+(e**-x))
plt.xlabel('Valores de X')
plt.title('Funcion tangencial')

plt.plot(x,f(x,e),linestyle='--',color='y')
plt.grid()

