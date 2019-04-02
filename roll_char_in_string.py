
# coding: utf-8

# In[61]:


st = "bca"
roll = [1,2,3]
list1=[]
list2=[]
st2=""
for i in range(0,len(st)):
    list1.append(st[i])
#print(list1)
for i in roll:
    n = i
    for j in range(0,n):
        list1[j] = chr(ord(list1[j])+1)
        #print(list1[j])
#print(list1)
for i in list1:
    
    st2 = st2+i
print(st2)

