# L1000-repurposing
Drug repurposing with L1000 data
## RNA-seq data processing 
After getting RNA-seq data, first quantify them with Salmon(https://github.com/COMBINE-lab/salmon). 

In R(DE_Deseq_AD.r),install"tximeta" and "DESeq2". Import the quantified data and process them into differential expression profiles. Top differential expressed genes can then be used in next step as disease signatures.

In python(calc_ES.py), use the up and down regulated gene as disease signature to calculate Enrichment Score(ES) against L1000 disease profiles. The drugs with lowest negative scores can be used as candidates to reverse the disease state.

