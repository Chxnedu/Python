# [] to create lists
friends = [ "stanley", "chxnedu", "ugo", "kachi"]
enemies = [ "brock", "lexi", "nate"]

# the .extend combines the 2 lists
# friends.extend(enemies)

# friends.append("olisa")
# the .append() is used to add an item to the end of a list
# with .append(), the item always gets added to the end of the list

# the .insert() is used to add an item to a particular place in a list. it takes 2 values, the index and the item
# all the other items after it get pushed to the right
# friends.insert(0, "kelvin")

# you can remove elements with .remove()
# friends.remove("ugo")
# to clear a list entirely, use .clear()
# friends.clear()

# to check if a particular element is in a list, use print(friends.index("name"))
# if it's in the list, it'll return the index of the element, if not it'll return an error
# print(friends.index("kachi"))

# you can use .sort() to sort the elements in ascending order
friends.sort()

# .copy to copy lists
friends2 = friends.copy()


print(friends2)