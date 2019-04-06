
# coding: utf-8

# In[2]:


def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        print('{a}  {b}'.format(a=i,b=_binary(i)))
    
def _binary(number):
    st=""
    while(number>0):
        rem = number%2
        number = number//2
        st+=str(rem)
    st = st[::-1]
    return st

    return st
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

