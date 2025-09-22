#CHAPTET 4 PYTHON (WORKING WITH LISTS)
#for loop
friends=['ram','sham','bheem','rahul','sharma']
for friend in friends:
    print(f"Sending the invitation to {friend.title()}.")

#statement out of loop
magic=['alice','davis','carolina']
for mag in magic:
    print(f"{mag.title()},that was a greate trick !")
    print(f"I cant wait to see your next trick,{mag.title()}.\n")
print(f"Thank you,everyone.That was a great magic show !")

#range
for value in range(1,9):
    print(value)

even_number=list(range(2,11,2))
print(even_number)

odd_number=list(range(1,10,2))
print(odd_number)
#list
number=list(range(1,6))
print(number)







