my_dict = {'1': 'Mayukh', '2': 'Kundan', '3': 'Kusal'} 
my_dict.clear() 
print(my_dict)

d = {'Name': 'Mayukh', 'Age': '23', 'Country': 'India'} 
print(d.get('Name')) 
print(d.get('Gender')) 
print(list(d.items())[1][0]) 
print(list(d.items())[1][1]) 
print(list(d.keys())) 
print(list(d.values()))

d2 = {'Name': 'Kundan', 'Age': '24'}  
d1.update(d2) 
print(d1)

d = {'Name': 'Mayukh', 'Age': '23', 'Country': 'India'} 
d.pop('Age') 
print(d)

d = {'Name': 'Mayukh', 'Age': '23', 'Country': 'India'} 
d.popitem() 
print(d)
d.popitem() 
print(d)

#Output:
#{}
#Mayukh
#None
#Mayukh
#23
#['Name', 'Age', 'Country']
#['Mayukh', '23', 'India']
#{'Name': 'Kundan', 'Age': '24', 'Country': 'India'}
#{'Name': 'Mayukh', 'Country': 'India'}
#{'Name': 'Mayukh', 'Age': '23'}
#{'Name': 'Mayukh'}
