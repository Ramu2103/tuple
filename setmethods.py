#Set Methods
a={'rahul','raj','sonam','rani'}
b={'sumit','rahul','python','java'}
print("A:",a)
print("B:",b)
print()

#intersection() method
#returns item which exists in both sets
ism=a.intersection(b)
print("Intersection:", ism)
print()

#Union() Method
#Returns all items from original set and all items from specified set
um=a.union(b)
print("union: ",um)
print()


#difference() Method
#returns items that exist only in first set and not in both sets
dm=a.difference(b)
print("Difference: ",dm)
print()