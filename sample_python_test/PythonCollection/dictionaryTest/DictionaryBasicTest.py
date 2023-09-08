class DictionaryBasicTest:
    print("Start Testing ")

    # Creating a Dictionary
    my_dictionary = {
        "name": "Pankaj",
        "location": "India",
        "employee_id": 123456,
        "age": 30

    }
    print("my_dictionary ", my_dictionary)

    # Creating a Dictionary
    my_dictionary = {
        "name": "Ranjan",
        "location": "UK",
        "employee_id": 123457,
        "age": 35
    }
    print("my_dictionary location --> ", my_dictionary['location'])

    # Python - Access Dictionary Items
    # You can access the items of a dictionary by referring to its key name, inside square brackets
    name = my_dictionary['name']
    print("name", name)

    # We can use get() method also to get the result
    name = my_dictionary.get("name")
    print("name", name)

    # The keys() method will return a list of all the keys in the dictionary
    all_keys = my_dictionary.keys()
    print("All Keys", all_keys)

    # The values() method will return a list of all the values in the dictionary
    all_values = my_dictionary.values()
    print("All Values", all_values)

    # The items() method will return each item in a dictionary, as tuples in a list
    all_item = my_dictionary.items()
    print("All Item", all_item)

    # If we update the Key/Value - it will be updated
    my_dictionary["Gender"] = "male"
    my_dictionary["location"] = "India"
    # The update() method will update the dictionary with the items from the given argument
    my_dictionary.update({"age": 40})
    # We can add into dictionary
    my_dictionary["Language"] = "English"
    my_dictionary.update({"last_name": "Singh"})

    print("Keys & Values after update")
    print("All Keys", all_keys)
    print("All Values", all_values)
    print("All Item", all_item)

    # Check if "keys" exist in the dictionary
    if "employee_id" in my_dictionary:
        print("Yes , It's exist")
    else:
        print("Not Exist")
    # Alternative
    if "employee_id" in all_keys:
        print("Yes , It's exist")
    else:
        print("Not Exist")
    # Check if Value exist
    if "India" in all_values:
        print("Yes , It's exist")
    else:
        print("Not Exist")

    # Remove Item - We can use pop() / popitem() / del keyword to remove item from Dictionary
    # The pop() method removes the item with the specified key name
    my_dictionary.pop("last_name")
    print("All Item after POP", my_dictionary)

    # The popitem() method removes the last inserted item
    my_dictionary.popitem()
    print("All Item after popitem ", my_dictionary)

    # The del keyword removes the item with the specified key name
    del my_dictionary["name"]
    print("All Item after del item ", my_dictionary)

    # The clear() method empties the dictionary
    my_dictionary.clear()
    print("All Item after Clearing item ", my_dictionary)

    # The del keyword can also delete the dictionary completely
    del my_dictionary
    print("All Item after del item ", my_dictionary)
    # NameError: name 'my_dictionary' is not defined - Since Dictionary has been deleted





