#Remove word from list using function method

def rem(list,word):
    for item in list:
        list.remove(word)
        return list

list=["sneha","ram","som"]
print(rem(list,"som"))
