import re

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "This is a secret much. It's a coming access, but it's spending him with a weeks."
"

# Decrypt the ciphertext using Caesar cipher
decrypted_text = ""
for shift in range(26):
    decrypted_text = caesar_decrypt(ciphertext, shift)

# Find all occurrences of the pattern \w+ in the decrypted text
matches = re.findall(r'\w+', decrypted_text)

# Print the found matches
if matches:
    for match in matches:
        print("Flag found:", match)
else:
    print("No flag found.")
