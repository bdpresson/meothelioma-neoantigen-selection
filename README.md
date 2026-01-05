# meothelioma-neoantigen-selection
Aimed to help characterize tumor-infiltrating lymphocytes (TILs) in resectable MPM treated with neoadjuvant ICB combination therapy to uncover the immunologic basis of this response in mammalian cell cultures.

Process protein FASTA sequences using netMHCpan 4.1 to data mine and identify candidate immunogenic tumor antigens associated with mesothelioma: rearrangemnet genes, mesothelioma-specific genes, and tumor-associated antigens, cancer testis antigens, and human endogenous retroviruses.

Developed and deployed Python-based scripts to streamline the preprocessing of raw datasets mined from netMHCpan, utilizing automation to reduce manual data handling of millions of data points.

1) Identify biomarkers of interest.
2) Visit the NIH National Library of Medicine (https://www.ncbi.nlm.nih.gov/) and select the protein database, search gene, then filter for Homo sapiens.
3) Select for FASTA file(s) with full aa sequence; precursors are acceptable. Do NOT select isoforms.
4) Copy and paste the FASTA standard text to netMHCpan 4.1: https://services.healthtech.dtu.dk/services/NetMHCpan-4.1/
5) Select "8mer", "9mer", and "10mer" under "Peptide Length."
6) Select (or copy and paste) for specific HLA haplotypes associated with patients in clinical study. Note: HLA supertypes may be appropriate in other contexts, but it is out of the mesothelioma study.
7) Copy and paste text into a text file (.txt). Save the file(s) with a consistent nomenclature that includes the gene of interest (i.e., "MSLN_1", "MSLN_2", "MSLN_3")
8) If there are more than 20 haplotypes of interest, then repeat steps 5-7 until all haplotypes have been accounted for.
9) Use "compiler_netmhcpan_filter.script.py" to compile the .txt files and remove observations that do not include "WB" or "SB" in the "BindLevel" column. Be sure to follow the comments in the Python script to properly produce a .csv.

The .csv file is prepared for downstream analysis. 

The goal is to identify candidate neoantigen peptide sequences to test in mammalian cell cultures to analyze T-cell clonal dynamics in patients receiving ICB combination therapy.
