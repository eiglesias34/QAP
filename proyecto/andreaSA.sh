#!/bin/sh
python3 main.py qapdata/chr25a.dat qapsoln/chr25a.sln 1000 > resultadosTS/chr25a.txt
python3 main.py qapdata/lipa50a.dat qapsoln/lipa50a.sln 1000 > resultadosTS/lipa50a.txt
python3 main.py qapdata/tai25a.dat qapsoln/tai25a.sln 1000 > resultadosTS/tai25a.txt
python3 main.py qapdata/tai60a.dat qapsoln/tai60a.sln 1000 > resultadosTS/tai60a.txt
python3 main.py qapdata/tai64c.dat qapsoln/tai64c.sln 1000 > resultadosTS/tai64c.txt
python3 main.py qapdata/tai80a.dat qapsoln/tai80a.sln 1000 > resultadosTS/tai80a.txt
python3 main.py qapdata/tai100a.dat qapsoln/tai100a.sln 1000 > resultadosTS/tai100a.txt