#home price
home = input ("Enter condo price:")
homeprice = int (home)

downpayment = homeprice * 0.05

print (downpayment)

costs = input ("Enter closing costs:")
closingcosts = int (costs)

totalcosts = downpayment + closingcosts

print ("The total costs:", totalcosts)

monthlym = input ("Enter monthly ownership costs:")
monthlycosts = int (monthlym)

yearlycosts = monthlycosts * 12

print ("Your yearly ownership cost:", yearlycosts)

year5cost = yearlycosts * 5

print ("Your year 5 ownership costs:", year5cost)


#rent

rent = input ("Enter monthly rental costs:")
rental = int (rent)

ycosts = rental * 12

print ("Your yearly rental cost:", ycosts)

y5costs = ycosts * 5

print ("Your year 5 rental costs:", y5costs)
