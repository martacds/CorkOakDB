This repository includes everything that was used in [CorkOakDB](https://corkoakdb.org) to process data and implement changes.

### bioschemas
Constructed from documentation and tools provided by [Bioschemas](https://bioschemas.org).
Includes the section added to template.php and the .js file with the annotation. The resources annotated are Gene, Polypeptide, BioProject, BioSample and Organism.

### edit_GFF
Script to alter the original GFF file obtained from the article. Includes additional files with descriptions of polypeptides published prior to the draft genome and a file matching the current IDs of transcripts with the IDs of the first version of the portal.

### edit_IPS
An additional InterProScan file was created by substituting the polypeptide IDs for their respective gene IDs. Includes a file with this match.

### get_bestBLAST
Original script to get only the first and best hit from a BLAST file and edited script to also get any following entries that have the same values.

### get_expression
Pipeline that obtains the expression values of genes by BioSamples from a list of SRA numbers. Includes scripts for 454 (single-ended) and Illumina (paired-ended) datasets, with pre-processing and without, respectively. For the 454 datasets there are two configurations of tools for the pre-processing.
- **454 SE w. pp**: FASTQdump, TagCleaner, _Sickle, PrinSeq_, GMAP, SamTools, FeatureCounts, StringTie
- **454 SE w. pp (Trim)**: FASTQdump, TagCleaner, _Trimmomatic_, GMAP, SamTools, FeatureCounts, StringTie
- **Illumina PE wo. pp**: FASTQdump, HISAT2, SamTools, FeatureCounts, StringTie

#### biosample_xml
Template for the xml files necessary for the BioSample loader in Tripal.

#### fastaQual2fastq.pl
Script to convert FASTA + QUAL files to FASTQ. Obtained from https://github.com/josephhughes/Sequence-manipulation/blob/master/fastaQual2fastq.pl

#### tool_links
Links to all tools used in `get_expression`
