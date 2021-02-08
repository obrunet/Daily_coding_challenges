"""
Rotational cipher / Caesar cipher  - https://exercism.io/tracks/python/exercises/rotational-cipher/

The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using
an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular
arithmetic. The letter is shifted for as many values as the value of the key.
The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13.
A ROT13 on the Latin alphabet would be as follows:
    Plain:  abcdefghijklmnopqrstuvwxyz
    Cipher: nopqrstuvwxyzabcdefghijklm
It is stronger than the Atbash cipher because it has 27 possible keys, and 25 usable keys.
Ciphertext is written out in the same formatting as the input including spaces and punctuation.
Examples
    ROT5 omg gives trl
    ROT0 c gives c
    ROT26 Cool gives Cool
    ROT13 The quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
    ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The quick brown fox jumps over the lazy dog.
"""
 

def rotational_cipher(plain_text, rot_nb):
    """Recieve a string as plain_text / input, that once encrypted is return depending on the nb of rotation"""
    alpha_b, cipher_text = "abcdefghijklmnopqrstuvwxyz", ""
    rot_nb %= len(alpha_b)
    for letter in plain_text:
        new_letter = alpha_b[(alpha_b.index(letter) + rot_nb) % len(alpha_b)]
        cipher_text += new_letter
    return "".join(cipher_text)
 

def main():
    #letters in uppercase & spaces are not treated
    print(rotational_cipher("c", 0))
    print(rotational_cipher("cool", 26))
    print(rotational_cipher("omg", 5))
    print(rotational_cipher("thequickbrownfox", 13))
 

if __name__ == "__main__":
    main()