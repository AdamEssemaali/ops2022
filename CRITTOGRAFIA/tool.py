import argparse
import functions
from rich.console import Console
import os

console = Console()
parser = argparse.ArgumentParser(description="Crittografia")

parser.add_argument("-c", "--cifra", help="Cifra il testo", action="store_true")
parser.add_argument("-d", "--decifra", help="Decifra il testo", action="store_true")
parser.add_argument("-b", "--brute", help="Decifra il testo con brute force", action="store_true")
parser.add_argument("-ded", "--deduci", help="Deduci il testo", action="store_true")

parser.add_argument("-t", "--text", help="Testo da cifrare/decifrare", type=str)
parser.add_argument("-k", "--key", help="Chiave di cifratura", type=int)

parser.add_argument("-pc", "--parola_cifrata", help="Parola cifrata", action="append")
parser.add_argument("-pd", "--parola_decifrata", help="Parola decifrata", action="append")

args = parser.parse_args()



if args.cifra:
    try:
        console.print(functions.encrypt(args.text, args.key))
    except:
        console.print("Errore nella cifratura")

elif args.decifra:
    try:
        console.print(functions.decrypt(args.text, args.key))
    except:
        console.print("Errore nella decifratura")

elif args.deduci:
    text_array = []
    for i in range(len(args.parola_cifrata)):
        text_array.append((args.parola_cifrata[i], args.parola_decifrata[i]))

    functions.deduct(text_array, args.text)
elif args.brute:
    print("Brute force")
    print("Testo: " + args.text)
    functions.brute(args.text)
else:
    console.print("Nessuna azione selezionata")
