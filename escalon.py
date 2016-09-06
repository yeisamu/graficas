
# coding: utf-8

# In[4]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-2,2)
c=np.linspace(-1,1)
def f(x,c):
    return np.piecewise(x,[x<-c, x > c],[0,1,5])


# In[7]:

plt.xlabel('Valores de X')
plt.title('Funcion Escalon')

plt.axis([x[0], x[-1], -0.1, 1.5])
plt.plot(x,f(x,c),linestyle='--',color='c')
plt.grid()


# In[ ]:



