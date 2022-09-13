""" 
7. Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries.
 """



d1=dict(A=56,B=90,C=75)
d2=dict(X=89,Y=78,Z=45)
d3=dict(P=42,Q=87,R=82)

d4=dict(dx=d1,dy=d2,dz=d3)
print(d4)
#=====================================OUTPUT==================================
# {'dx': {'A': 56, 'B': 90, 'C': 75}, 'dy': {'X': 89, 'Y': 78, 'Z': 45}, 'dz': {'P': 42, 'Q': 87, 'R': 82}}