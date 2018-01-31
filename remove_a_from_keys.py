r= {'ashu':'123','shubhi':'456','shalini':'789'}
for item in r.keys():
    if 'a' in item:
        item1 = item.replace('a','')
        r[item1] = r.pop(item)
print(r)


        
    