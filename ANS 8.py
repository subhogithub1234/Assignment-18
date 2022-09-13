""" 
8. Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value.
 """

l1=[101,102,103,104]
l2=['Amit','Rohit','Suman','Payel']
d1={l1[i]:l2[i] for i in range(len(l1))}
print(d1)
#==================================OUTPUT======================================
# {101: 'Amit', 102: 'Rohit', 103: 'Suman', 104: 'Payel'}
  