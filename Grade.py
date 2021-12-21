def result () :
    score = input ("Enter Score:")

    try:
        grade = float (score)

        if grade > 1:
            print ("Not within required range, try again!")
            result()

        elif grade >= 0.9:
            print ("A")

        elif grade >= 0.8:
            print ("B")

        elif grade >= 0.7:
            print ("C")

        elif grade >= 0.6:
            print ("D")

        elif grade < 0.6:
            print ("F")

    except:
        print ("Not acceptable, try again!")
        result()

result ()

#simplest code yet. Good job! Let's keep going at it!
# a little more elegant!
