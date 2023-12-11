import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
# import random as r

c1 = st.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange'])
s1 = st.radio('선의 형태를 선택하시오', ['-', ':', '-.', '--'])

fig, ax = plt.subplots()

x = []
y = []
for i in range(-20, 21, 2):   
    x.append(i)
    y.append(3*i*i - 5*1 + 2)

# plt.plot(x,y, 'rs-', linewidth = 2)

plt.plot(x, y, color=c1, linestyle=s1, marker='h')


st.pyplot(fig)


import sys
# sys.exit()

fig, ax = plt.subplots()

x = []
for i in range(-00, 21, 15): 
# for i in range(-100, 100):
    i
    x.append(i/10.0)

col = st.columns(3)
with col[0]:
    a = st.number_input('Insert a', step = 1)
with col[1]:
    b = st.number_input('Insert b', step = 1)
with col[2]:
    c = st.number_input('Insert c', step = 1)

y = []
for i in x:
    y.append(a*i**2 + b*i + c)

plt.plot(x, y)
st.pyplot(fig)