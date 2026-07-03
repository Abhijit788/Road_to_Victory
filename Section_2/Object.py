num=90
print("id(",num,"):", id(num))
num=100
print("id(",num,"):", id(num))

hds =set()
tup=tuple([1,2,3])
tr=(1,2,3)
hds.add(tup)
print("id(tup):", id(tup))
hds.add(tr)
print("id(tr):", id(tr))
print("hds:", hds)