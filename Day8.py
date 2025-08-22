def Reverse_String(sentence):
  words = ""
  my_list = []

  for char in sentence:
    if char != " ":
      words = words + char 
    elif char == " ":
      if words != "":
        my_list.append(words)
        words = ""
  else:
    if words != "":
          my_list.append(words)
  my_list.reverse()
  final_string = " ".join(my_list)
  return final_string

sentence ="word"
print(Reverse_String(sentence))
