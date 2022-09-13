# 9. Write a python program to merge two python dictionaries into one dictionary.

d1={'A': 56, 'B': 90, 'C': 75}
d2={'X': 89, 'Y': 78, 'Z': 45}
d1.update(d2)
print(d1)
#=====================================OUTPUT=====================================
# {'A': 56, 'B': 90, 'C': 75, 'X': 89, 'Y': 78, 'Z': 45}