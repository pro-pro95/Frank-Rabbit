fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:

    stuff = line.split()
    for wds in stuff: #for loop within the for loop
        if wds in lst:
            continue
        if not wds in lst:
            lst.append(wds)
            lst.sort()
print (lst)


#tough because I was making the wrong moves.
