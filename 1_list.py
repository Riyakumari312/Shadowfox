#list of superheroes representing the justice league
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print(justice_league)
#task 1 : To find the number of members in justice league
Members = len(justice_league) #len() is used to find thw length of list
print(f"\n1.There are {Members} members in justice league")
#task 2 : To add Batgirl and Nightwing as new members
justice_league.append("Batgirl") #append is used to add a new string in the list
justice_league.append("Nightwing")
print(f"\n2.Justic league after adding Batgirl and Nightwing is {justice_league}")
#task3:As Wonder woman is the leader of the justice league we have to move her to beginning of the list
justice_league.pop(2) #pop(2) is used to remove string from position 2
justice_league.insert(0, "Wonder woman") #insert(0, "WonderWoman") is used to insert wonderwoman at position 2
print(f"\n3.Justic league after making wonder woman as the leader is {justice_league}")
#task 4:Due to conflicts between flash and Aquaman we need to separate them usinf Superman or Green Laltern
index_superman = justice_league.index("Superman") #index is used to find the position of  the string
justice_league.pop(index_superman)
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index+1, "Superwoman")
print(f"\n4.After inserting Superman in between Flash and Aquaman our justice league becomes {justice_league}")
#task 5:To assemble a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n5.After crisis Superman assembled a new team. The new team is:", justice_league)
#task 6: Arrange the team members alphabetically
justice_league.sort() # sort is used to arrange the words 
print(f"\n6.The team after arranging alphabetically: {justice_league}")
print(f"\nThe new leader of the team is: {justice_league[0]}")
