l1=[1,3,5,7,9,11,13]
l2=[2,4,6,8,10,12,14]
l3=[]

even_index = [l1[i] for i in range(1, len(l1),2)]
odd_index=[l2[i] for i in range(0,len(l2),2)]

l3 = even_index+odd_index

print(l3)
