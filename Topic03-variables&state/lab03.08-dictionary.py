# Maciej Izydorek
# creates dictionary, store hard coded book details
# outputs values in dictionary
currentBook = {
    'title' : 'Atomic habits',
    'author' : 'James Clear',
    'price' : '9.99'
}

# print dictionary object 
print(currentBook)
# print author
print(currentBook['author'])
# create and set attribute ISBN
currentBook['ISBN'] = '12345'
# print out all values in currentBook
print('---')
for book in currentBook.values():
    print ("{}".format(book))
