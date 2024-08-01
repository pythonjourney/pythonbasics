str1 = "P@#yn26at^&i5ve"

digits = []
letters = []
symbols = []

for i in range str1:
  if i.isdigit():
    digits.append(i)

  elif i.isalpha():
    letters.append(i)


  else:  symbols.append(i)


  print(len(digits)-1)
  print(len(letters)-1)
  print(len(symbols)-1)
     
