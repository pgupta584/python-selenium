class TupleTest:
    # CREATE TUPLE -----------
    # Create a sample tuple
    my_tuple = ("Cat", "Dog", "Hen", "Red")
    print("My Tuple --> ", my_tuple)

    # Duplicates are allowed
    my_tuple = ("Cat", "Dog", "Hen", "Red")
    print("My Tuple --> ", my_tuple)

    # Tuple Example with one element
    this_tuple = ("Cat",)
    print(this_tuple)

    # NOT a tuple
    this_tuple = ("Cat")
    print(this_tuple)

    # Tuple items can be of any data type
    my_tuple = ("John", 34, True, 12345678, "male")

    # It is also possible to use the tuple() constructor to make a tuple
    my_tuple = tuple(("John", 34, True, 12345678, "male"))  # note the double round-brackets
    print(my_tuple)

    # ACCESS TUPLE -----------
    # Getting length
    my_tuple_length = len(my_tuple)
    print("my_tuple_length --> ", my_tuple_length)

    # Getting 4th Element from List
    print("Getting 4th Element --> ", my_tuple[3])

    # Getting last element
    print("Getting last element--> ", my_tuple[-1])

    # Getting 2nd last element
    print("Getting 2nd last element -->", my_tuple[-2])

    # Getting item from ranges between 1 & 3 (Last index will be excluded)
    print("Getting item from ranges between 1 & 3 --> ", my_tuple[1:3])

    # Getting the items from the beginning to, but NOT including after index (Last index will be excluded)
    print("Getting the items from the beginning to, but NOT including --> ", my_tuple[:3])

    # Getting item starting from index till last index
    print("Getting item starting from index till last index --> ", my_tuple[1:])

    # Updating Tuple Value -
    my_tuple = ("John", 34, True, 12345678, "male")
    mylist = list(my_tuple)
    mylist[0] = "Tom"
    my_tuple = tuple(mylist)
    print("my_tuple after update ", my_tuple)

    # Add new element into Tuple - It's added as last element
    my_tuple = ("John", 34, True, 12345678, "male")
    mylist = list(my_tuple)
    mylist.append("Tom")
    my_tuple = tuple(mylist)
    print("my_tuple after adding tom  ", my_tuple)

    # Packing a Tuple
    animal = ("Cat", "Dog", "Hen")

    # Un-Packing a Tuple
    (Cat, Dog, Hen) = animal
    print(Cat)
    print(Dog)
    print(Hen)
    # We can Keep by changing the values also like - Store with their properties
    (meo, bhaubhau, kukuduku) = animal
    print("Animal Sounds meo is --> ", meo)
    print("Animal Sounds bhaubhau is --> ", bhaubhau)
    print("Animal Sounds kukuduku is --> ", kukuduku)

    # Packing a Tuple
    animal = ("Cat", "Dog", "Hen", "Red", "Blue", "White")

    # We can Keep by changing the values also like - Store with their properties
    (meo, bhaubhau, kukuduku, *color) = animal
    print("Animal Sounds meo is --> ", meo)
    print("Animal Sounds bhaubhau is --> ", bhaubhau)
    print("Animal Sounds kukuduku is --> ", kukuduku)
    print("Color is --> ", color)

    # Iterating tuple --------------------------

    # Iterating tuple item using Loop
    my_new_tuple = ["John", 34, True, 12345678, "male"]
    print("Iterating tuple item")
    for i in my_new_tuple:
        print(i)

    # Iterating tuple index using Loop
    print("Iterating tuple index")
    for i in range(len(my_new_tuple)):
        print(i)

    # tuple items by using a while loop
    print("Iterating tuple item using while loop")
    i = 0
    while i < len(my_new_tuple):
        print(my_new_tuple[i])
        i = i + 1

    # Joining tuple --------------

    # Join Two tuple
    tuple_1 = ("John", 34, True, 12345678, "male")
    tuple_2 = ("Bangalore", 1234567890)
    tuple_3 = tuple_1+tuple_2
    print("tuple_3 ", tuple_3)

    # Multiply Tuple
    multiply_tuple = tuple_2*3
    print("multiply_tuple ", multiply_tuple)

    # Tuple Count Method
    tuple_4 = (5, 3, 5, 8, 7, 5, 4, 3, 8, 5)
    x = tuple_4.count(5)
    print("5 occurred ", x)

    # Find first index of a number
    tuple_4 = (5, 3, 5, 8, 7, 5, 4, 3, 8, 5)
    x = tuple_4.index(3)
    print("3 occurred 1st at index ", x)


