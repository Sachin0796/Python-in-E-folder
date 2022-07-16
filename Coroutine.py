# lets say we are creating a searcher function which will find a word in dictionary and its taking time to read the dictionary from some memory location everytime we are running a searcher function. In this case, we will create it as a coroutine where loading dictionary from the function will done once and searching will be done as per words given

def searcher():
    import time
    book="This is a book in sachin's folder for searching any word"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("Word found")
        else:
            print("Word not found")

search=searcher()
print("Reading book from memory")
next(search)
print("Loading book to the local is completed")
# search.send(None)
search.send("sachin")
search.send("This")
search.send("that")
search.close()