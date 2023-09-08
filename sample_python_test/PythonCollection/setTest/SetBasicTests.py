class SetTest:
    # Create a sample Set
    my_set = {"Cat", "Dog", "Hen"}
    print("my_set --> ", my_set)

    # Duplicate values will be ignored
    my_set = {"Cat", "Dog", "Hen", True}
    print("my_set with duplicate --> ", my_set)

    # True and 1 is considered the same value
    my_set = {"Cat", "Dog", "Hen", True, 1}
    print("my_set with duplicate --> ", my_set)

    # Get the number of items in a set - Duplicates will be ignored
    my_set = {"Cat", "Dog", "Hen", True, 1}
    print("my_set Length ", len(my_set))

    # Set items can be of any data type
    my_set = {"Cat", "Dog", "Hen", True, 1, 123456, 'c'}
    print("my_set items ", my_set)

    # Know Data type for Set
    my_set = {"Cat", "Dog", "Hen", True, 1, 123456, 'c'}
    print("Data type for Set ", type(my_set))

    # Using the set() constructor to make a set
    my_set = set(("Cat", "Dog", "Hen", True, 1, 123456, 'c'))
    print("Data type for Set ", my_set)

    # Iterating Set value
    my_set = {"Cat", "Dog", "Hen", True, 1}
    print("Iterating set Values")
    for i in my_set:
        print(i)

    # Adding item to Set -----------------

    # set use the add() method
    my_set = {"Cat", "Dog", "Hen", True}
    my_set.add("Ant")
    print("my_set after adding new item", my_set)

    # Add items from another set into the current set, use the update() method
    set_1 = {"Cat", "Dog", "Hen", True}
    set_2 = {"Ant", "Pig"}
    set_1.update(set_2)
    print("my_set after adding new set", set_1)

    # Add List into set , use the update() method
    set_1 = {"Cat", "Dog", "Hen", True}
    set_2 = ["Ant", "Pig"]
    set_1.update(set_2)
    print("my_set after adding new list", set_1)

    # Removing item from Set --------

    # Remove Item from Set using remove - If the item to remove does not exist, remove() will raise an error.
    my_set = {"Cat", "Dog", "Hen", True}
    my_set.remove(True)
    print("my_set after removing an item", my_set)

    # Remove Item from Set using discard - If the item to remove does not exist, discard() will NOT raise an error.
    my_set = {"Cat", "Dog", "Hen", True}
    my_set.discard("Cat")
    print("my_set after removing an item", my_set)

    # Remove a random item by using the pop() method - The return value of the pop() method is the removed item
    my_set = {"Cat", "Dog", "Hen", True}
    item_removed = my_set.pop()
    print("removed item", item_removed)
    print("my_set after removing an item", my_set)

    # clear() method empties the set
    my_set = {"Cat", "Dog", "Hen", True}
    my_set.clear()
    print("my_set after clearing", my_set)

    # del keyword will delete the set completely
    my_set = {"Cat", "Dog", "Hen", True}
    # del my_set
    # print("my_set after clearing", my_set) # Item will be deleted so we will get an error

    # Joining Two Sets ---------------------

    # The union() method returns a new set with all items from both sets
    set1 = {"Cat", "Dog", "Hen"}
    set2 = {1, 2, 3}
    set3 = set1.union(set2)
    print("New Set after add ", set3)

    # The update() method inserts the items in set2 into set1
    set1 = {"Cat", "Dog", "Hen"}
    set2 = {1, 2, 3}
    set3 = set1.update(set2)
    print("New Set after add ", set3)

    # The intersection_update() method will keep only the items that are present in both sets
    set1 = {"Cat", "Dog", "Hen"}
    set2 = {1, 2, 3, "Cat"}
    set1.intersection_update(set2)
    print("New Set after intersection_update ", set1)

    # The intersection() method will return a new set, that only contains the items that are present in both sets.
    set1 = {"Cat", "Dog", "Hen"}
    set2 = {1, 2, 3, "Cat"}
    set3 = set1.intersection(set2)
    print("New Set after intersection_update ", set3)

    # The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
    set1 = {"Cat", "Dog", "Hen"}
    set2 = {1, 2, 3, "Cat"}
    set1.symmetric_difference_update(set2)
    print("New Set after symmetric_difference_update ", set1)

    # symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
    set1 = {"Cat", "Dog", "Hen"}
    set2 = {1, 2, 3, "Cat"}
    set3 = set1.symmetric_difference(set2)
    print("New Set after symmetric_difference ", set3)

    # Copy the Set into another Variable
    set1 = {"Cat", "Dog", "Hen"}
    set2 = set1.copy()
    print("Copied Set ", set2)
