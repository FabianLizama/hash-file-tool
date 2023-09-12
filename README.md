<h1 align=center>
File Hashing Tool
</h1>
<p align=center>
<span>Herramienta de manejo de file hashes</span>
<br>
</p>
<span>
Estaba a punto de descargar software de dudosa procedencia y decidí crear mi propio programa para comparar hashes por diversión.
</span>


## Instalación
```console
# clonar el repositorio
$ git clone https://github.com/fabianlizama/file-hash-tool.git

# cambiar el directorio a file-hash-tool
$ cd file-hash-tool
```
## Uso
```console
$ python hash --help
usage: hash.py [-h] [-a {md5,sha1,sha256,sha512}] [-v {0,1,2}] [-o OUTPUT] [-i INPUT | -H HASH] file

Read the hash of a file and compare it with another hash

positional arguments:
  file                  File to hash

options:
  -h, --help            show this help message and exit
  -a {md5,sha1,sha256,sha512}, --algorithm {md5,sha1,sha256,sha512}
                        Hahing algorithm
  -v {0,1,2}, --verbosity {0,1,2}
                        Verbosity level
  -o OUTPUT, --output OUTPUT
                        Output file
  -i INPUT, --input INPUT
                        Input file to comparate
  -H HASH, --hash HASH  Input hash
```

Para leer el hash de un archivo (SHA256 por defecto):
```
python hash.py file
```

Para cambiar el feedback por consola (Niveles 0, 1 y 2):
```
python hash.py file -v 0
```

Para elegir el algoritmo (md5 por ejemplo):
```
python hash.py file -a md5
```

Para escribir el hash en un archivo de salida:
```
python hash.py file -o outputFile.txt
```

Para comparar el hash por uno introducido por consola:
```
python hash.py file -H hashString
```

Para comparar el hash por uno escrito en un archivo:
```
python hash.py file -i inputFile
```
