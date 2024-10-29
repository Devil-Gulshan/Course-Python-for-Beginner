s1 = { 8,76,45,56}
s2 = { 8,23,56 ,7}
print ( s1.union(s2))
print(s1.intersection(s2))
print({8,87}.issuperset(s1)) # chack the values s1 set 8,87 to output false
print(s1.issuperset({8,76})) # chack the values s1 set 8,76 to output true
print (s1.difference(s2)) # chack the difference s1 sets and s2 sets to output is {76,45}
