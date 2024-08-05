
# strings are immutable
newstr = "Python"

size = len(newstr)

print(f"length of newstr is {size}")

print(newstr[0])

count = 0

while count < size:
      for i in newstr:
       print(i, count, f"Iteration{count}")
       count += 1

      




