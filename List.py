# List

fname = input("Enter file name: ")
fh = open(fname)
lst = list() # words from text file stored here
for line in fh:

    stuff = line.split() # split text file into individual words.
    for wds in stuff: # check if word already exists in list and store if not.
        if wds in lst:
            continue
        if not wds in lst:
            lst.append(wds)
            lst.sort() 
print (lst)

