def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = []
    key_index = 0

    for c in ciphertext:
        if c.isalpha():
            c_val = ord(c) - ord('A')
            k_val = ord(key[key_index % len(key)]) - ord('A')
            p_val = (c_val - k_val) % 26
            plaintext.append(chr(p_val + ord('A')))
            key_index += 1
        else:
            plaintext.append(c)

    return ''.join(plaintext)