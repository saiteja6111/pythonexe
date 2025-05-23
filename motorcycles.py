car_brands = ['honda','bmw','pagani','mazada','toyota','ford']

car_brands[0] = 'benz'#changing elements in the list by assigning with indexes

print(car_brands)

car_brands.append('Bugati')#adding elements at the end of the list

print(car_brands)

motor_cycles = []

motor_cycles.append('yamaha')

motor_cycles.append('suzuki')

motor_cycles.append('tvs')

print(motor_cycles)


#we can add the elements in the list at a particular position using insert method

fruits = ['apple','banana','pineapple']

print(fruits)
fruits.insert(1,'grapes')

print(fruits) 

del fruits[2]#use the del statement to remove elements 

print(fruits)


#we can remove the items from a list at last using pop method or by indexing

li_1 = ['hello','world','mewo','cat']

li_1.pop(1)

print(li_1)

#removing item by value

li_1.remove('mewo')

print(li_1)


