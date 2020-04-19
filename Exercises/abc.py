def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

print(string_splosion("Dobry"))

def old_macdonald(name):
    return name[0].upper() 
print(old_macdonald("old_macdonald"))
