#!/usr/bin/env python
# coding: utf-8

# ### 一、一个简单的绘图例子

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


fig, ax = plt.subplots()  # 创建一个包含一个axes的figure
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # 绘制图像


# - 另一种方法

# In[4]:


plt.plot([1,2,3,4],[3,2,5,4])


# ### 二、Figure的组成

# - Figure：顶层级，用来容纳所有绘图元素
# 
# - Axes：matplotlib宇宙的核心，容纳了大量元素用来构造一幅幅子图，一个figure可以由一个或多个子图组成
# 
# - Axis：axes的下属层级，用于处理所有和坐标轴，网格有关的元素
# 
# - Tick：axis的下属层级，用来处理所有和刻度有关的元素
# ![269a5697ad37c63a906c47c8d0bb6c6aa59911ed.png](attachment:269a5697ad37c63a906c47c8d0bb6c6aa59911ed.png)

# ### 三、两种绘图方式

# 1. 显式创建figure和axes，在上面调用绘图方法，也被称为OO模式（object-oriented style)
# 
# 2. 依赖pyplot自动创建figure和axes，并绘图

# In[5]:


x = np.linspace(0, 2, 100)

fig, ax = plt.subplots()  
ax.plot(x, x, label='linear')  
ax.plot(x, x**2, label='quadratic')  
ax.plot(x, x**3, label='cubic')  
ax.set_xlabel('x label') 
ax.set_ylabel('y label') 
ax.set_title("Simple Plot")  
ax.legend() 


# In[6]:


x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear') 
plt.plot(x, x**2, label='quadratic')  
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()


# In[ ]:




