# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 16:08:29 2025

@author: bpresso1
"""

import pandas as pd
import re
from glob import glob
import os

# Include 'SourceFile' in your column headers
columns = ['Pos', 'MHC', 'Peptide', 'Core', 'Of', 'Gp', 'Gl', 'Ip', 'Il', 'Icore', 'Identity', 'Score_EL', '%Rank_EL', 'BindLevel', 'SourceFile']

# Regex for lines ending with SB/WB
pattern = re.compile(r'^(.*?)\s+<=\s*(SB|WB)\s*$')

all_filtered_rows = []


# Read text file(s) into Python string
for filename in glob('ACRBP_*.txt'):       ### Change file name here
    with open(filename, 'r') as f:
        document = f.read()

    lines = document.strip().split('\n')
    data_start = False

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if "Pos" in line and "BindLevel" in line:
            data_start = True
            continue
        if not data_start or line.startswith('-'):
            continue

        m = pattern.match(line)
        if m:
            main_text, bindlevel = m.group(1), m.group(2)
            parts = main_text.split()
            if len(parts) == 13:
                row = parts + [bindlevel] + [os.path.basename(filename)]     ### Adds new column with file names, furthest right.
                all_filtered_rows.append(row)
            else:
                print(f"Skipping unparsable row in {filename}: {line}")


# Write combined CSV with SourceFile column
if all_filtered_rows:
    df = pd.DataFrame(all_filtered_rows, columns=columns)
    df.to_csv('filtered_peptides_ACRBP.csv', index=False)       ### Create a name for the new .csv file here
    print(f"Filtered rows from {len(glob('ACRBP_*.txt'))} files have been saved to 'filtered_peptides_ACRBP.csv'.") # Change what the text, 
else:                                                                                                               # specifically the gene should say here
    print("No filtered rows found in any files.")