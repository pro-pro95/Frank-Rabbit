# Code to calculate email average spam confidence

fname = input("Enter file name: ")
fh = open(fname)
count = 0
confidence = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1

        position = line.find('0')
        number = float (line [position: position+6])
        confidence = confidence + number

spam = confidence/count

print ("Average spam confidence:", spam)

