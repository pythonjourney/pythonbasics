#str1 = PyNaTive

#problem: Take KuBeRnetEs and print in the order of lower case to upper case

str1 = "KuBeRnetEs"

  #uenetsKBRE

lowerstr = []
upperstr = []
for i in str1:

   if i.islower():
      lowerstr.append(i)
   else:
        
        if i.isupper():
           upperstr.append(i)


lowupp = lowerstr + upperstr

lowuppjoin= "".join(lowupp)
print(lowuppjoin)



