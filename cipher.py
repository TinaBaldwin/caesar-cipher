# add your code here

result = ""
shift = 5

sentence = str(input("Please enter a sentence: "))

for character in sentence:
    if character.isalpha(): 
        shift_alpha = ord(character) + shift 
        if character.islower() and shift_alpha > ord("z"):
           shift_alpha -= 26        
        elif character.isupper() and shift_alpha > ord("Z"):
            shift_alpha -= 26
        encrypted_letter = chr(shift_alpha)
        result += encrypted_letter
    else:
        result += character 

print("The encrypted sentence is: ", result)
