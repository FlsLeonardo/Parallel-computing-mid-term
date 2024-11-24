# Parallel-computing-mid-term
![Version](https://img.shields.io/badge/CrntVersion-02.07-dc00ff)
![Author](https://img.shields.io/badge/Author-Falsarolo_Leonardo-6800ff)
![Languages](https://img.shields.io/badge/Languages-C++-0070ff)
![Languages](https://img.shields.io/badge/Languages-Python-00ffd4)
![About](https://img.shields.io/badge/Languages-Matrix_transposition-lightblue)


**#C++ #Python #Benchmark #Graph #Matrix_transposition #OpenMP #Compile_option #Data**

# Parallel-computing-mid-term


## Description
- The goal of this project is to explore and implement parallel computing techniques to optimize the performance of computationally intensive tasks.
---
## Requirements

- C++
- C++ libs
    * iostream
    * vector 
    * cstdlib 
    * ctime 
    * cmath
    * random
    * omp.h
    * fstream

- Python
- python libs (pip install)
    * sys
    * matplotlib
    * numpy 
    * pandas 
---
## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/FlsLeonardo/Parallel-computing-mid-term/tree/main

# Go into the repository
$ cd Parallel-computing-mid-term
```
## Example of execution (Cli , FULL)
Once downloaded the folder and opend it in your CMD
```cmd
> cd method1/bin
> ./compile.sh
---------- wait end execution ----------
> pyton graph.py
---------- wait end execution ----------

> cd ../..
> cd method2/bin
> ./compile.sh
---------- wait end execution ----------
> pyton graph.py
---------- wait end execution ----------

> cd ../..
> cd method3/bin
> ./compile.sh
---------- wait end execution ----------
> pyton graph.py
---------- wait end execution ----------

cd ../..
> pyton best_Implicit_for_matrix_dimension.py
---------- wait end execution ----------
```
compiler.sh has different execution strategies also..
```bash
    Compile.sh $1 $2
    # $1 Compiler Option
    # $2 Matrix Dimension Option
```

- Possiility of selecting one or more Compiler Option 
    - example: ``` > Compile.sh "O1 -funroll-loops" ```
- Possiility of choosing the Compiler Option and the matrix size if you wonnna do a sigle matrix transposition execution with a specific compiler option
    - example: ``` > Compile.sh "O1 -funroll-loops" 10 ```

(BY default the compiler.sh will done the Full execution)


## Esempio di esecuzione (CLI, only for a specific type of compiler Option)
```

```
- E' possibile eseguire il programma in modalità grafica eseguendo `pingsweeper_gui.py`

lista di parametri utilizzabili:
- `--help` Informazioni base per l'esecuzione del programma
- `--url` Imposta l'url per il caricamente nel db
- `--tkn` Imposta il token necessario all'autenticazione per il db
- `--subnet` Imposta la rete dove effetuare la ricerca
- `--file` Modalità di esecuzione dove si cerca all'interno di `flussi/computers.csv` gli indirizzi da scannerizzare

(_Di default verrà effettuata la scannerizzazione della rete 192.168.1.0/24_)

Esempio di esecuzione con più parametri:
```
py pingsweeper.py --subnet= 192.168.1.0/24 --url=https://agenttest-cgrg.harperdbcloud.com --tkn=Y29ybmVsZ3JnXzprZDROTHB5NUwjNmhNITI=
```
---

## Key Features

* Sync Scrolling
  - While you type, LivePreview will automatically scroll to the current location you're editing.
* GitHub Flavored Markdown  
* Syntax highlighting
* [KaTeX](https://khan.github.io/KaTeX/) Support
* Dark/Light mode
* Toolbar for basic Markdown formatting
* Supports multiple cursors
* Save the Markdown preview as PDF
* Emoji support in preview :tada:
* App will keep alive in tray for quick usage
* Full screen mode
  - Write distraction free.
* Cross platform
  - Windows, macOS and Linux ready.