



#I searched for the topic through w3schools 

list1 = [1,3,4,4,5,7,6,8,7,1]
result = {}

for num in list1:
   if num in result:
       result[num] += 1
   else:
       result[num]= 1

print(result)


