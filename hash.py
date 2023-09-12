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
        print_verbosity(2, f"Abriendo archivo: {args.file}")
        print_verbosity(2, f"Algoritmo: {args.algorithm}")
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
    print_verbosity(1, "El archivo no existe")
    sys.exit(1)
except PermissionError:
    print_verbosity(1, "No tienes permisos para abrir el archivo")
    sys.exit(1)
except IsADirectoryError:
    print_verbosity(1, "El archivo es un directorio")
    sys.exit(1)
except Exception as e:
    print_verbosity(1, "Error desconocido")
    print_verbosity(2, e)
    sys.exit(1)

print_verbosity(0, HASHSTRING, True)
print_verbosity(1, f"Hash extraido: {HASHSTRING}")

# Comparación de hashes

# Hash introducido por consola
if args.hash:
    print_verbosity(1, f"Hash introducido: {args.hash}")
    if args.hash.isupper():
        args.hash = args.hash.lower()
    if HASHSTRING == args.hash:
        print_verbosity(0, True, True)
        print_verbosity(1, "El hash coincide")
    else:
        print_verbosity(0, False, True)
        print_verbosity(1, "El hash no coincide")

# Hash introducido por archivo
if args.input:
    print_verbosity(1, f"Abriendo archivo: {args.input}")
    try:
        with open(args.input, "r", encoding="utf-8") as f:
            HASHSTRING = f.read()
            f.close()
    except FileNotFoundError:
        print_verbosity(1, "El archivo no existe")
        sys.exit(1)
    except PermissionError:
        print_verbosity(1, "No tienes permisos para abrir el archivo")
        sys.exit(1)
    except IsADirectoryError:
        print_verbosity(1, "El archivo es un directorio")
        sys.exit(1)
    except Exception as e:
        print_verbosity(1, "Error desconocido")
        print_verbosity(2, e)
        sys.exit(1)

# Output del hash extraido
if args.output:
    print_verbosity(1, f"Guardando hash en {args.output}")
    try:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(HASHSTRING)
            f.close()
    except PermissionError:
        print_verbosity(1, "No tienes permisos para abrir o crear el archivo")
        sys.exit(1)
    except IsADirectoryError:
        print_verbosity(1, "El archivo es un directorio")
        sys.exit(1)
    except Exception as e:
        print_verbosity(1, "Error desconocido")
        print_verbosity(2, e)
        sys.exit(1)
