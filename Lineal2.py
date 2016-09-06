
# coding: utf-8

# In[16]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-3,3,0.1)


# $$f(x)=4x+1 $$

# In[23]:

y=x 
plt.xlabel('Valores de X')
plt.title('Funcion lineal')
plt.plot(x,y,linestyle='--',color='r')
plt.grid()

