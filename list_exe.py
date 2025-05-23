#3-4 exe

friends = ['hari','bharath','aman']

print(f"{friends[0]}!, come to the party \n{friends[1]}!, lets enjoy the party come \n{friends[2]}!, visit my home to party at evening")

#3-5

print(f"{friends[0]}! can not come to party!, i am inviting new one")
friends.remove('hari')
friends.insert(0,'saiteja')
print(f"{friends[0]}!, come to the party \n{friends[1]}!, lets enjoy the party come \n{friends[2]}!, visit my home to party at evening")


#3-6
print("\n\n I found a bigger table")

friends.insert(0,'ramteja')
friends.insert(2,'ganesh')
friends.append('chaitanya')

#3-7
print("the dinner table has only two spaces left!")
friends.pop(0)
friends.pop(1)
friends.pop(2)
friends.pop(2)

print(friends)

del friends[0]
del friends[0]

print(friends)


#lists in order 

cars = ['bugati','pagani','lambogrgini','mclarine','astromartin','bmw','benz','koinsegg']
cars.sort(reverse=True)
print(cars)

#to print list sorted in temporary by sorted() function

print(sorted(cars))
print(cars)
cars.reverse()

print(cars)

#we can find the length of a list using len() function

print(len(cars))