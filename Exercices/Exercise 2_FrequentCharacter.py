name="stuccessttt"
char_count ={}
for char in name:
    if char in char_count:
       char_count[char]+=1
    else:
       char_count[char]=1


if(char_count):
    max_char = max(char_count, key = char_count.get)
    max_count = char_count[max_char]
    print(f"The most frequent occurred character is {max_char} which occured {max_count} times")
else:
    print("You didnt enter any character")



