def decrypt_caesar(ciphertext, shift):
    decrypted_text = ''
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

ciphertext = "Uijt jt b tfdsfu nvdi. Ju't b dpnjoh bddftt, cvu ju't tqfoejoh ijn xjui b xfflt"

for i in range(26):
    decrypted = decrypt_caesar(ciphertext, i)
    print(f"Shift {i}: {decrypted}")
