""" 
4. Write a python program to change the value of a specific item by referring to its key
name.
 """

d1={101:'Amit',102:'Rohit',103:'Suman',104:'Payel'}
print(d1)
print("After edit.......")
d1[102]="Subham"
print(d1)
#===============================================OUTPUT==============================
""" 
{101: 'Amit', 102: 'Rohit', 103: 'Suman', 104: 'Payel'}
After edit.......
{101: 'Amit', 102: 'Subham', 103: 'Suman', 104: 'Payel'} """