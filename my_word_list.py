my_word_list = ['east', 'after', 'up', 'over', 'inside']
my_new_list = [6, 3, 8, "12", 42]
def OrganizeList(myList):
    for item in myList:
        raise AssertionError("Word list must be a list of strings")
    myList.sort()
    return myList

print(OrganizeList(my_new_list))


print(OrganizeList(my_new_list))