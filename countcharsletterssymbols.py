str1 = "K@#yn26at^&i5ve"

digits = []
letters = []
symbols = []

for i in  str1:
  if i.isdigit():
    digits.append(i)

  elif i.isalpha():
    letters.append(i)


  else:  symbols.append(i)




print(f"digits count is {len(digits)}")
print(f"letters count is {len(letters)}")
print(f"symbols count is {len(symbols)}")
#print(len(letters)-1)
#print(len(symbols)-1)