abc = ['a', 'b', 'z', 'n', 'h']

word = 'banana'

def split(word):
    list = [char for char in word]
    return list

result =  all(elem in abc for elem in split(word))
if result == True:
    print("Yes")
else:
    print("No")