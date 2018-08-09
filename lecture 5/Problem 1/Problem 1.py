
# coding: utf-8

# # Newton Fractal 

# In[1]:


# import packages
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# constants
# tolerance
epsilon = 1e-4
# the range of x
X = np.linspace(-2, 2, num=10000)
width = X.shape[0]
# the range of y
Y = np.linspace(-2, 2, num=10000)
height = Y.shape[0]
# max number of iteration
MAXIT = 20
# list for storing the time of iteration
itTime = []
# the fucntion determines the times of iteration
# the result will be appended to a list
# def deterIt(z, lst, z0=1, err=epsilon, MAX=MAXIT):
#     cnt = 0
#     z1 = z
#     while ((cnt < MAX) & (np.abs(z1 - z0) < err)):
#         z1 = z1 - (z1 ** 3 - 1) / (3 * z1 ** 2)
#         cnt += 1
#     lst.append(cnt)


# In[3]:


# clear the list
itTime.clear()
# traverse the complex plane
# to get raw data
for y in Y:
    for x in X:
        # deterIt(x + y* 1j, itTime)
        # print(x + y* 1j)
        z = x + y * 1j
        cnt = 0
        while ((cnt < MAXIT) & (np.abs(z - 1) > epsilon)):
               z = z - (z ** 3 - 1) / (3 * z ** 2)
               cnt = cnt + 1
        
        itTime.append(cnt)

# In[37]:


# take the complementary
image = np.array(itTime)
# image= MAXIT - image
image = image.reshape((width, height))
image.shape


# In[38]:


# visualization
plt.figure()
plt.imshow(image, cmap=plt.cm.hot_r)
plt.colorbar()
plt.show()


