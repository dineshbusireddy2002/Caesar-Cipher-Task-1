def encrypt(text, shift):
    result = ""
    
    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Keep other characters as is (e.g., spaces, punctuation)
        else:
            result += char
    
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? (Type 'Q' to quit): ").upper()
        
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice not in ['E', 'D']:
            print("Invalid choice. Please try again.")
            continue
        
        text = input("Enter your message: ")
        shift = int(input("Enter shift value: "))
        
        if choice == 'E':
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted message: {encrypted_text}")
        elif choice == 'D':
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
