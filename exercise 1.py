menu=['dosa','idle','rice','chapathi']
for m in menu:
    print(f"Monday morning to evening the food which is aviable is {m}. ") 
print("\nAdding a new item..")
menu.append('mini cake')
print(f"The Final menu is:{menu}")

#copying list
my_foods=['pizza','falafel','carrot cake']
friends_food=my_foods[:]
my_foods.append('cannoli')
friends_food.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\n friends favorite foods are:")
print(friends_food)

#tuples
game=('fire','water','smile','cry')
print(game[1])
game[0]=('earth')

