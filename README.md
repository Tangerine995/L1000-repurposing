# L1000-repurposing
Drug repurposing with L1000 data
## RNA-seq data processing 
After getting RNA-seq data, first quantify them with Salmon(https://github.com/COMBINE-lab/salmon). 

In R(DE_Deseq_AD.r),install"tximeta" and "DESeq2". Import the quantified data and process them into differential expression profiles. Top differential expressed genes can then be used in next step as disease signatures.
## L1000 data

The Library of Integrated Cellular Signatures (LINCS) is an NIH program which funds the generation of perturbational profiles across multiple cell and perturbation types, as well as read-outs, at a massive scale. The LINCS Center for Transcriptomics at the Broad Institute uses the L1000 high-throughput gene-expression assay to build a Connectivity Map which seeks to enable the discovery of functional connections between drugs, genes and diseases through analysis of patterns induced by common gene-expression changes.



| Description                               | Download                                      |
| ----------------------------------------- | --------------------------------------------- |

| Plate control *z*-scores                  | [Bayesian_GSE70138_Level4_ZSPC_n335465x978.h5](http://callisto.astro.columbia.edu/files/L1000/Bayesian_GSE70138_Level4_ZSPC_n335465x978.h5)<br>[Bayesian_GSE92742_Level4_ZSPC_n1093191x978.h5](http://callisto.astro.columbia.edu/files/L1000/Bayesian_GSE92742_Level4_ZSPC_n1093191x978.h5)|
| Combined *z*-scores by bio-replicates     | [Bayesian_GSE70138_Level5_COMPZ_n116218x978.h5](http://callisto.astro.columbia.edu/files/L1000/Bayesian_GSE70138_Level5_COMPZ_n116218x978.h5)<br>[Bayesian_GSE92742_Level5_COMPZ_n361481x978.h5](http://callisto.astro.columbia.edu/files/L1000/Bayesian_GSE92742_Level5_COMPZ_n361481x978.h5)|
| signature IDs |GSE70138_Broad_LINCS_sig_info_2017-03-06.txt.gz(https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fsig%5Finfo%5F2017%2D03%2D06%2Etxt%2Egz)|
| perturbagen information  |GSE70138_Broad_LINCS_pert_info_2017-03-06.txt.gz(https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fpert%5Finfo%5F2017%2D03%2D06%2Etxt%2Egz) |



### Data stuctures

The *z*-score results (as HDF5) are compatible with those published by L1000 group. Each of them contains three datasets as follows:

* `/colid` are the signature IDs (Level 5) or instance IDs (Level 4);

* `/rowid` are the names of landmark genes;

* `/data` are the *z*-scores as a matrix.

Full meta data are available from the publication by L1000 group: [GSE70138](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE70138) and [GSE92742](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742). They include perturbagen and cell line information associated with signature and instance IDs in the datasets.


## Calculate enrichment score(ES)
In python(calc_ES.py), use the up and down regulated gene as disease signature to calculate Enrichment Score(ES) against L1000 disease profiles. The drugs with lowest negative scores can be used as candidates to reverse the disease state.

## results

