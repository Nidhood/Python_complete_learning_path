print("**<List section>\n")
list_1 = [1, 4, 5, 3, 2]
print("* We have the list ---------------------> ", list_1[0:])
list_1_size = len(list_1)
print("* The size of the list ----------------->  ", list_1_size, "")
new_list = list_1 + [10, 7, 9, 6, 8]
print("* The new list is ----------------------> ", new_list[0:])
new_list.append(str('Number list 0 to 10'))
print("* Adding new element to the new list ---> ", new_list)
popped_item = new_list.pop(10)
print("* Popped item --------------------------> [", popped_item, "]")
print("* The new list is ----------------------> ", new_list[0:])
new_list.sort()
print("* The sorted list is -------------------> ", new_list)
print("\n**<Dictionaries>\n")
dictionary_1 = {"Key 1": "value 1", "key 2": "value 3"}
print("* Example of a dictionary is -----------> ", dictionary_1)
print("* Accessing to the value 1 -------------> ", dictionary_1["Key 1"])
dictionary_2 = {"Apple": 2.99, "Oranges": 1.99, "Milk": 5.90}
print("* My catalog of supermarket product is -> " + str(dictionary_2))
print("* Unit price of apple is : ", dictionary_2["Apple"], ", Oranges price is : ", dictionary_2["Oranges"],
      ", Milk price is : ", dictionary_2["Milk"])
dictionary_3 = {"k1": 123, "k2": [0, 1, 2], "k3": {"insideKey": 100}}
print("* My catalog of dictionary number 3 is = Key #1 : ", dictionary_3["k1"], ", Key #2 : ", dictionary_3["k2"],
      ", Key #3 : ", dictionary_3["k3"])
print("* Is accessible the keys into another keys any time it requires like : ", dictionary_3["k2"][2], ", ",
      dictionary_3["k3"]["insideKey"])
dictionary_4 = {"key1": ['a', 'b', 'c']}
capital_letter = dictionary_4["key1"][2].upper()
print("* Using dictionaries optimizes the proces of searching data, like : ", capital_letter)
dictionary_5 = {"key1": 100, "key2": 200}
print("* To add a new key into the dictionary '", dictionary_5, "' is like : ", end="")
# end="" is used to indicate to the console for doesn't print a new line :D
dictionary_5["key3"] = 300
print(dictionary_5)
dictionary_5["key1"] = int(dictionary_5['key1'] / 2)
print("* Or if needs replace any value of a specific key it will works like : ", dictionary_5)
print("* If needs search only the name of the keys it will work like : ", dictionary_5.keys())
print("* If needs search only the name of the values of each key it will work like : ", dictionary_5.values())
print("* It can also allows to search the content of all catalog of (items or elements) the dictionary like : ",
      dictionary_5.items())
print("\n**<Tuples>\n")
# A difference between tuples with dictionaries or lists, is that you  can't replace elements from the default set,
# in other words it's immutability. And obviously it uses parenthesis
# an assignment object to a tuple will drop an error.
tuple_1 = (1, 2, 3)
list_2 = [1, 2, 3]
print("* Example of a tuple : ", tuple_1)
print("* As you can see when you write the type of the array it will show : ", type(tuple_1), " and ", type(list_2))
print("* Like another list you can see the size of the tuple like : ", len(tuple_1))
print("* Like another list you can see the index position like : ", tuple_1[0])
tuple_2 = ('a', 'a', 'b')
print("* Additional functionality that can be used a difference between a list, is like : ", tuple_2.count('a'))
print("* Also you can search the specific index position of a element into the tuple like : ", tuple_2.index('b'))
print("\n***<Sets>\n")
# Like a mathematics view, is like unordered collections of unique elements.
set_1 = set()
print("* Example of an empty set : ", set_1)
set_1.add(1)
print("* Adding new element to de set : ", set_1)
set_1.add(2)
print("* Adding another element : ", set_1)
set_1.add(2)
print("* But it doesn't changes when you add a repetitive element (¡Because sets support only unique elements!): ",
      set_1)
list_3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
set_2 = set(list_3)
print("* It will print the unique elements : ", set_2)
print("\n**<I/O Basics files>\n")
print(
    "* It only works in jupyter-notebook:\n* Create a new file_1.txt in the current path  = %%Writefile file_1.txt.txt', and next in the "
    "same editor space you can write the text that the file_1.txt will contain.")
print("* To set a pointer into the file_1.txt created before in jupyter-notebook : file_1.txt = open('file_1.txt.txt').")
print("* To find the current path if needs more specific 'pwd' ")
print("* file_1.txt.read() = will show in the console all the text into the pointer file_1.txt.")
# [¡Advertise!]: if we put again file_1.txt.read() it wil show <''>, that's because in the first use of the function .read()
# the pointer will read all the text since he arrives to the end, and it will stay there, so when we call again the
# function .read() the pointer will be there in the same end position, so logically it will show <''>
print("* file_1.txt.seek(0) will put the pointer in the 0 position of the file_1.txt (in the beginning), so you can call again the "
      "function file_1.txt.read() without problems to show his content.")
print("* You can assign the content of the file_1.txt into a variable like : contents =  file_1.txt.read()")
print("* You can read each line of the text an put separately into a list like : file_1.txt.readlines()")
# ¡Be careful! is not the same rules to open files' pathway between Widows or macOS and Linx.
# In Widows, we use the path form like : "c:\\Users\\Username\\Folder\\test.txt"
# In macOS, we use the path form like : "/Users/YourUserName/Folder/file_1.txt.txt"
print("* Always we need to close our pointer files, in the form : file_1.txt.close()")
# We will use the nex indentation form of code to indicate that in te pointer 'my_new_file' will realize all the
# instructions below, that's always close the proces leaving the indentation form (more efficient).
with open('../Files/file_1.txt') as my_new_file:
    contents_1 = my_new_file.read()
    # Don't worry to close the file_1.txt, this indentation form automatically close the pointer 'my_new_file'
with open('../Files/file_1.txt', mode='r') as my_new_file:
    contents_2 = my_new_file.read()
    # Here we addition short change, that indicate the method of open the file_1.txt,
    # In this case we use 'r' that means read only.
    # 'w' means write mode only.
    # 'a' means append monde (adding more lines in the end of the file_1.txt).
    # 'r+' means read and write method.
    # 'w+' means read and write method, also if the file_1.txt name doesn't exist it creates the new file_1.txt!.
with open('../Files/file_1.txt', mode='a') as my_new_file:
    my_new_file.write("\nFOUR ON FOURTH")
# The next code allows to create a new file:
with open('../Files/file_2.txt', mode='w') as my_new_file:
    my_new_file.write("¡I'M BACK BITCHES!\n")
    