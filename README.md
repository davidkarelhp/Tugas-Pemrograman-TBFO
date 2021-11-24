# Tugas-Pemrograman-TBFO
Tugas Besar IF2124 Teori Bahasa Formal dan Otomata Compiler Bahasa Python

## Directories
    .
    ├── doc                             # Documentation files (Laporan tugas besar)
    ├── src                             # Source files
    │    ├── lib                        # library CFG2CNF
    │    ├── grammar                    # CNF and CFG grammar
    │    │    ├── CFG.txt               # CFG grammar
    │    │    └── CNF.txt               # CNF grammar
    │    ├── fa.py                      # Program for Finite Automata
    │    ├── parserprogram.py           # Main Program including CYK
    │    ├── readCNF.py                 # Program for reading CNF
    │    └── token.py                   # Program for toknizing input
    └── README.md

## How to Run

### Creating new CNF grammar from CFG
1. Pastikan directory pada `./Tugas-Pemrograman-TBFO`
2. Jalankan
    ```
    python3 src/lib/CFG2CNF/CFG2CNF.py src/grammar/CFG.txt    
    ```

### Using Parser Program
1. Pastikan directory pada `./Tugas-Pemrograman-TBFO/src`
2. Jalankan <br />
    - Windows:
    ```
    py parserprogram.py <nama_file>
    ```
    - MacOS and Unix:
    ```
    python parserprogram.py <nama_file>
    ```