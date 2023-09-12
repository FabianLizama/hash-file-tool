'''
Programa que calcula el hash de un archivo
Puede compararlo con otro hash introducido por el usuario si es necesario
También permite guardar el hash en un archivo de salida
'''

import hashlib
import argparse
import sys


# Argument parser
parser = argparse.ArgumentParser(
    description="Read the hash of a file and compare it with another hash"
)
group = parser.add_mutually_exclusive_group()
parser.add_argument("file", help="File to hash")
parser.add_argument("-a",
                    "--algorithm",
                    help="Hahing algorithm",
                    choices=["md5", "sha1", "sha256", "sha512"],
                    default="sha256")
parser.add_argument("-v",
                    "--verbosity",
                    help="Verbosity level",
                    type= int,
                    choices=[0, 1, 2],
                    default=1)
parser.add_argument("-o", "--output", help="Output file")
group.add_argument("-i", "--input", help="Input file")
group.add_argument("-H", "--hash", help="Input hash")

args = parser.parse_args()

def print_verbosity(verbosity, message, strict=False):
    '''
    Recibe un nivel de verbosity y un mensaje, lo imprime si el nivel de
    verbosity es mayor o igual al nivel de verbosity del programa. Si strict
    es True, solo imprime si el nivel de verbosity es exactamente igual al
    nivel de verbosity del programa.
    '''
    if strict:
        if args.verbosity == verbosity:
            print(message)
    else:
        if args.verbosity >= verbosity:
            print(message)

# Hashing
try:
    with open(args.file, "rb") as f:
        data = f.read()
        print_verbosity(2, f"Opening file: {args.file}")
        print_verbosity(2, f"Algorithm: {args.algorithm}")
        if args.algorithm == "md5":
            HASHSTRING = hashlib.md5(data).hexdigest()
        elif args.algorithm == "sha1":
            HASHSTRING = hashlib.sha1(data).hexdigest()
        elif args.algorithm == "sha256":
            HASHSTRING = hashlib.sha256(data).hexdigest()
        elif args.algorithm == "sha512":
            HASHSTRING = hashlib.sha512(data).hexdigest()
        f.close()
except FileNotFoundError:
    print_verbosity(1, "File does not exist")
    sys.exit(1)
except PermissionError:
    print_verbosity(1, "You don't have permission to open the file")
    sys.exit(1)
except IsADirectoryError:
    print_verbosity(1, "The file is a directory")
    sys.exit(1)
except OSError:
    print_verbosity(1, "The file is not a text file")
    sys.exit(1)

print_verbosity(0, HASHSTRING, True)
print_verbosity(1, f"Hash readed: {HASHSTRING}")

# Comparación de hashes

# Hash introducido por consola
if args.hash:
    print_verbosity(1, f"Input hash: {args.hash}")
    if args.hash.isupper():
        args.hash = args.hash.lower()
    if HASHSTRING == args.hash:
        print_verbosity(0, True, True)
        print_verbosity(1, "The hashes match")
    else:
        print_verbosity(0, False, True)
        print_verbosity(1, "The hashes don't match")

# Hash introducido por archivo
if args.input:
    print_verbosity(1, f"Opening file: {args.input}")
    try:
        with open(args.input, "r", encoding="utf-8") as f:
            HASHSTRING = f.read()
            f.close()
    except FileNotFoundError:
        print_verbosity(1, "The file does not exist")
        sys.exit(1)
    except PermissionError:
        print_verbosity(1, "You don't have permission to open the file")
        sys.exit(1)
    except IsADirectoryError:
        print_verbosity(1, "The file is a directory")
        sys.exit(1)
    except OSError:
        print_verbosity(1, "The file is not a text file")
        sys.exit(1)

# Output del hash extraido
if args.output:
    print_verbosity(1, f"Saving hash in: {args.output}")
    try:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(HASHSTRING)
            f.close()
    except PermissionError:
        print_verbosity(1, "You don't have permission to open the file")
        sys.exit(1)
    except IsADirectoryError:
        print_verbosity(1, "The file is a directory")
        sys.exit(1)
    except OSError:
        print_verbosity(1, "The file is not a text file")
        sys.exit(1)
