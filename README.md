# Drug repurposing with L1000 data
Screen L1000 dataset for drug candidates. 


## RNA-seq data processing 
After getting RNA-seq data, first quantify them with [Salmon](https://github.com/COMBINE-lab/salmon). You will need a FASTA file containing your reference transcripts and a (set of) FASTA/FASTQ file(s) containing your reads to run Salmon.

In R(DE_Deseq_AD.r),install"tximeta" and "DESeq2". Import the quantified data from Salmon and process them into differential expression profiles. See [guide](https://bioc.ism.ac.jp/packages/2.14/bioc/vignettes/DESeq2/inst/doc/beginner.pdf) to Deseq2 for more information.

Top differential expressed genes can then be used in next step as disease signatures. 

## L1000 data
### Summary

The Library of Integrated Cellular Signatures ([LINCS](https://lincsproject.org/LINCS/)) is an NIH program which funds the generation of perturbational profiles across multiple cell and perturbation types, as well as read-outs, at a massive scale. We build a pipeline, in parallel with L1000 group, to process raw fluorescent intensity data into *z*-scores as perturbagen signatures, available at [L1000-bayesian](https://github.com/njpipeorgan/L1000-bayesian). Our Level 4 and Level 5 data are equivalent to Level 4 and Level 5 data provided by L1000. Pre-computed datasets covering a majority of LINCS L1000 Phase I and Phase II is available in [Downloads](#Downloads) and [Zenodo](https://zenodo.org/record/5559183#.YWJS39rMKUk).



### Downloads
Bayesian L1000 data
| Description                               | Download                                      |
| ----------------------------------------- | --------------------------------------------- |
| Plate control *z*-scores                  | [Bayesian_GSE70138_Level4_ZSPC_n335465x978.h5](http://callisto.astro.columbia.edu/files/L1000/Bayesian_GSE70138_Level4_ZSPC_n335465x978.h5)<br>[Bayesian_GSE92742_Level4_ZSPC_n1093191x978.h5](http://callisto.astro.columbia.edu/files/L1000/Bayesian_GSE92742_Level4_ZSPC_n1093191x978.h5)|
| Combined *z*-scores by bio-replicates     | [Bayesian_GSE70138_Level5_COMPZ_n116218x978.h5](http://callisto.astro.columbia.edu/files/L1000/Bayesian_GSE70138_Level5_COMPZ_n116218x978.h5)<br>[Bayesian_GSE92742_Level5_COMPZ_n361481x978.h5](http://callisto.astro.columbia.edu/files/L1000/Bayesian_GSE92742_Level5_COMPZ_n361481x978.h5)|

Meta data
| Description                               | Download                                      |
| ----------------------------------------- | --------------------------------------------- |
| Signature IDs |[GSE70138_Broad_LINCS_sig_info_2017-03-06.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fsig%5Finfo%5F2017%2D03%2D06%2Etxt%2Egz)<br>[GSE92742_Broad_LINCS_sig_info.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742%5FBroad%5FLINCS%5Fsig%5Finfo%2Etxt%2Egz)|
| Perturbagen information  |[GSE70138_Broad_LINCS_pert_info_2017-03-06.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fpert%5Finfo%5F2017%2D03%2D06%2Etxt%2Egz)<br>[GSE92742_Broad_LINCS_pert_info.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742%5FBroad%5FLINCS%5Fpert%5Finfo%2Etxt%2Egz)|
|Cell information | [GSE70138_Broad_LINCS_cell_info_2017-04-28.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fcell%5Finfo%5F2017%2D04%2D28%2Etxt%2Egz)<br>[GSE92742_Broad_LINCS_cell_info.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742%5FBroad%5FLINCS%5Fcell%5Finfo%2Etxt%2Egz)|
|Gene information|[GSE70138_Broad_LINCS_gene_info_2017-03-06.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fgene%5Finfo%5F2017%2D03%2D06%2Etxt%2Egz)<br>[GSE92742_Broad_LINCS_gene_info.txt.gz](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742%5FBroad%5FLINCS%5Fgene%5Finfo%2Etxt%2Egz)|

Full meta data are available from the publication by L1000 group: Phase I [GSE92742](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742) and Phase II[GSE70138](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE70138). They include perturbagen and cell line information associated with signature and instance IDs in the datasets.For more informationabout LINCS L1000 data, see [Connectopedia](https://clue.io/connectopedia/)

### Data stuctures

The *z*-score results (as HDF5) are compatible with those published by L1000 group. Each of them contains three datasets as follows:

* `/colid` are the signature IDs (Level 5) or instance IDs (Level 4);

* `/rowid` are the names of landmark genes;

* `/data` are the *z*-scores as a matrix.



### Data Preparation for drug screening
1. Download L1000 data.
   Download the following files in folder L1000_data : Bayesian_GSE70138_Level5_COMPZ_n116218x978.h5, Bayesian_GSE92742_Level5_COMPZ_n361481x978.h5, GSE92742_Broad_LINCS_sig_info.txt.gz, GSE70138_Broad_LINCS_sig_info_2017-03-06.txt.gz. Then unzip xxx_sig_info.txt.gz files. 
2. Prepare up and down regulated genes.
   The up and down regulated genes produced by Deseq2 or other pilelines. Save them in up_genes.csv and down_genes.csv seperately. Note that the genes needs to be converted to official Gene Symbol. You can use a [converter](https://www.biotools.fr/human/refseq_symbol_converter) to do this.

### Calculate enrichment score(ES) and search for drug candidates
Use our pipeline (L1000_repurposing.ipynb) to search for drug candidates. 

Or in python(calc_ES.py), use the up and down regulated gene as disease signature to calculate Enrichment Score(ES) against L1000 profiles. The drugs with lowest negative Enirchment Scores can be used as candidates to reverse the disease state.

### Analysis your results
The screening results will contain a long list of drugs. You can further check their experiment information, target or structure to find the best candidate.

## Citation

Oliveros, Giovanni, et al. "Multi-scale predictive modeling discovers Ibudilast as a polypharmacological agent to improve hippocampal-dependent spatial learning and memory and mitigate plaque and tangle pathology in a transgenic rat model of Alzheimer’s disease." bioRxiv (2021).

Qiu, Yue, et al. "A Bayesian approach to accurate and robust signature detection on LINCS L1000 data." Bioinformatics 36.9 (2020): 2787-2795.

