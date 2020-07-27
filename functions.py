# Creating a function most_frequent that takes a string and prints its letters in decreasing order of their frequency.
def most_frequent():
    given_string= str(input("Please enter a string: "))
    res = {}
    for keys in given_string:
      res[keys] = res.get(keys, 0) + 1
    print("The letters in the given string with their frequencies: ",res)
    import operator
    sorted_res = dict(sorted(res.items(), key=operator.itemgetter(1),reverse=True))
    print("Letters in decreasing order of their frequencies: ",sorted_res)
most_frequent()
