import hashlib

with open("salt.txt", "r") as f:
  salt = f.read().strip()

myMap = {}
#make a dictionary from the rockyou words aka dictionary attack
with open("rockyou.txt", "r", encoding='latin-1') as f:
  for line in f:
    # strip new line character
    password = line.strip()
    # concat salt and password, encode to utf-8
    salted_password = (salt + password).encode('utf-8')
    # hash salted password
    hash_value = hashlib.sha256(salted_password).hexdigest()
    myMap[hash_value] = password

#add the bruteforce attack to the dictionary
arr = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '<', '>', '?']

for a in arr:
  for b in arr:
    for c in arr:
      for d in arr:
        for e in arr:
          val = (salt + a + b + c + d).encode('utf-8')
          newVal = hashlib.sha256(val).hexdigest()
          myMap[newVal] = (a + b + c + d)

with open("hashes.txt", "r") as f:
  for line in f:
    line = line.strip()
    if myMap.get(line) is not None:
      print(line, ": ", myMap[line], " ")
    else:
      print(line, ": ")