Codes developed to extract information from haplotype blocks (Haploview output) for further analysis of GWAS with haplotypes.

# Order of use of scripts
First use the python-markers.py script to extract haplotype block information from the Haploview output.
Next, use the mtx_sparse_hap.R script to extract, in a sparse array, the markers that form the haplotype blocks.

# To use the script in Python
Open the script and modify the directory.
To run on the terminal, use:
```Bash
$ python3 python-markers.py
```

# To use the script in R
Open the script and modify the directory.
To run on the terminal, use:
```Bash
$ R CMD BACTH mtx_sparse_hap.R
```