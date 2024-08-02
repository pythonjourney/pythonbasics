f = open("appendfile.txt", "a")
f.write("keep coding")
s="\nPython journey"

for i in range(0,5):
 f.write(s)
f.close()
