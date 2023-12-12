#!/bin/bash

# Change to the directory containing the Bril files
cd ../test/benchmarks/core/

# Run the command on all files
for file in *.bril; do
    bril2json < "$file" | python main.py -o "${file%.bril}.asm"
done
