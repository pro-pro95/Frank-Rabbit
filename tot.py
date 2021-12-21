largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        anum = int (num)

        if largest is None:
            largest = anum
        elif largest < anum:
            largest = anum

        if smallest is None:
            smallest = anum
        elif smallest > anum:
            smallest = anum
    except:
        print ("Invalid input")
        continue
        
print("Maximum is", largest)
print ("Minimum is", smallest)
