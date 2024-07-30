# we'll  be opening all our files using with
# with statement is added to language in python 2.5
#if we use with we will miss to close out the file

file = open('cloud.txt', 'r')

for line in file:
    print(line)

file.close()