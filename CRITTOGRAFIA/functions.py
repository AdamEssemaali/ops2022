import rich
from rich.console import Console
import string

console = Console()
alphabet = string.ascii_lowercase

def find_in_dict(value,dictionary): 
    for key, val in dictionary.items():
        if value in val:
            return key

def split_vocabulary():
    words = open("vocabulary_re.txt", "r").read().split("\n")
    new = {}
    c = None
    for i in words:

        if i[0] != c:
            c = i[0]
            new[c] = [i]
        else:
            new[c].append(i)

    
    return new






def encrypt(text, key):
    encrypted = ""
    for i in range(len(text)):
        char = text[i]
        if char in alphabet:
            encrypted += alphabet[(alphabet.index(char) + key) % len(alphabet)]
        else:
            encrypted += char
    return encrypted

def adjust_key(key):
    while key > len(alphabet):
        key -= len(alphabet)
    return key

def decrypt(text, key):
    decrypted = ""
    key = adjust_key(key) if key > len(alphabet) else key

    for i in range(len(text)):
        char = text[i]
        if char in alphabet:
            decrypted += alphabet[(alphabet.index(char) - key) % len(alphabet)]
        else:
            decrypted += char
    return decrypted

def reconstruct_vocabulary_from_cifrated(text_array):
    voc = {}
    for i in text_array:
        for dec_letter, cifr_letter in zip(i[0], i[1]):
            voc[dec_letter] = cifr_letter
    


    return voc

def get_key_from_vocabulary(vocabulary):
    first_letter = list(vocabulary.keys())[0]
    original_letter = alphabet[alphabet.find(vocabulary[first_letter])]
    key = alphabet.find(original_letter) - alphabet.find(first_letter)

    return abs(key)



def deduct(text_array, cifrated_text):
    reconstructed_voc = reconstruct_vocabulary_from_cifrated(text_array)
    key = get_key_from_vocabulary(reconstructed_voc)
    console.print(f"Key: {key} - Text: {decrypt(cifrated_text, key)}", style="bold green")
    return decrypt(cifrated_text, key)

def check_vocabulary_word(word, vocabulary: dict):
    if word[0] not in vocabulary.keys(): 
        return False
    if word in vocabulary[word[0]]:
        return True
    else:
        return False
    
def check_vocabulary(text, vocabulary):
    words = text.split(" ")
    n = 0
    c = 0
    while c < len(words):
        if check_vocabulary_word(words[c], vocabulary):
            n += 1
        c += 1
    if n > 0:
        return True
    else:
        return False
    
def brute(text):
    for i in range(len(alphabet)):
        v = check_vocabulary(decrypt(text,i), split_vocabulary())
        if v:
            console.print(f"Key: {i} - Text: {decrypt(text,i)}", style="bold green")
            return decrypt(text,i)
    
    console.print("Nessuna parola italiana riconosciuta lista di chiavi tentate:\n", style="bold red")
    for i in range(len(alphabet)):
        console.print(f"Key: {i} - Text: {decrypt(text,i)}", style="bold red")
