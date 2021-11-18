library("tximeta")
colfile="~\\data\\coldata.txt"
coldata <- read.csv(colfile, stringsAsFactors=FALSE)

indexdir="~\\data\\genome\\Homo_sapiens.GRCh38_index\\"
fastadir="~\\data\\genome\\Homo_sapiens.GRCh38.cdna.all.fa"
gtfPath="ftp://ftp.ensembl.org/pub/release-100/gtf/homo_sapiens/Homo_sapiens.GRCh38.100.gtf.gz"
makeLinkedTxome(indexDir=indexdir, source="Ensembl", organism="Homo sapiens",
                release="100", genome="GRCh38", fasta=fastadir, gtf=gtfPath, write=FALSE)

se <- tximeta(coldata)
gse <- summarizeToGene(se)


library("DESeq2")
dds <- DESeqDataSet(gse, design = ~ diagnosis)
dds <- DESeq(dds)
res <- results(dds)
resOrdered <- res[order(res$padj),]
write.csv(as.data.frame(resOrdered), file="~\\data\\DE_AD_all.csv")
