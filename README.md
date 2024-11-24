# Parallel-computing-mid-term
![Version](https://img.shields.io/badge/CrntVersion-02.07-dc00ff)
![Author](https://img.shields.io/badge/Author-Falsarolo_Leonardo-6800ff)
![Languages](https://img.shields.io/badge/Languages-C++-0070ff)
![Languages](https://img.shields.io/badge/Languages-Python-00ffd4)
![About](https://img.shields.io/badge/About-Matrix_transposition-lightblue)


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
The full execution will do all the possible matrix transpositions and methods with all different pre setted compilation flags. 

Once downloaded the folder and opend it in your CMD.
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
### Compiler.sh parameters
`compiler.sh` has different execution strategies also..
```bash
    Compile.sh $1 $2
    # $1 Compiler Option
    # $2 Matrix Dimension Option
```

- Possiility of selecting one or more Compiler Option 
    - example: ``` > Compile.sh "O1 -funroll-loops" ```
- Possiility of choosing the Compiler Option and the matrix size if you wonnna do a sigle matrix transposition execution with a specific compiler option
    - example: ``` > Compile.sh "O1 -funroll-loops" 10 ```

(_B default the compiler.sh will done the Full execution_)


## Example of execution (CLI, only for a specific type of compiler Option)
Chose one method from:
- **method1** Serial Approach Matrix transposition with 2 for loop nested each startin from 0 to n (where n is the size of the matrix)
- **method2** Optimized Serial Approach Matrix transposition with Block-based Transposition  
- **method3** Optimized Serial Approach Matrix transposition with Diagonal Approach

Then go to the correct folder via `CLI`  (from the main folder)
```cmd
Parallel-computing-mid-term>  cd "Method_chosen"/bin
```
Execute the following command 
```python
Parallel-computing-mid-term/"Method_chosen"/bin>  ./Compile.sh "O2"
```
Or for more Compilation flag
```python
Parallel-computing-mid-term/"Method_chosen"/bin>  ./Compile.sh "O2 -funroll-loops"
```
- Is it possible also to execute `python graph.py` that does all the graphs thanks to the `files.csv` in the output folder
### Graph.py parameters
list of command executable for `graph.py`:
- `--help` all information for the execution
- `-type=("serial,"implicit","omp")` does the graph for only one file.csv ("serial,"implicit","omp")
- `-ES` does the **efficency** and **speedup** graphs for the OpenMP parallelization

(_By default the file graph.py does all the file and all the possible functions_)

## Example of execution (CLI with compiler Option and given matrix size)
Chose one method from:
- **method1** Serial Approach Matrix transposition with 2 for loop nested each startin from 0 to n (where n is the size of the matrix)
- **method2** Optimized Serial Approach Matrix transposition with Block-based Transposition  
- **method3** Optimized Serial Approach Matrix transposition with Diagonal Approach

Then go to the correct folder via `CLI`  (from the main folder)
```cmd
Parallel-computing-mid-term>  cd "Method_chosen"/bin
```
Execute the following command 
```python
Parallel-computing-mid-term/"Method_chosen"/bin>  ./Compile.sh "O2" 10
```
Or for more Compilation flag
```python
Parallel-computing-mid-term/"Method_chosen"/bin>  ./Compile.sh "O2 -funroll-loops" 10
```
- Is it possible also to execute `python graph.py` that does all the graphs thanks to the `files.csv` in the output folder