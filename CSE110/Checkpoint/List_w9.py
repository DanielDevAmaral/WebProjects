friends = []
new_friends = ""

while new_friends != friends:
    print("Type END if you want to stop the list")
    print()
    new_friends = input("Type a name of a friend: ")
    print()
    friends.append(new_friends)
    
    if new_friends.lower() == "end":
        friends.remove("end")
        break
   
print("Your friends are: ")

for friend in friends:
    print(friend)