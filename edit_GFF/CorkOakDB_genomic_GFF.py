# SCRIPT TO EDIT THE GENOMIC.GFF FILE TO THE SPECIFIC REQUIREMENTS OF CORKOAKDB
# Marta Silva, 2020

### changes mRNA, tRNA, rRNA, lnc_RNA, snRNA, snoRNA to transcript
### adds polypeptide line w/ CDS info
### adds descriptions to polypeptides from previous literature
### adds matching EST IDs from old portal to transcripts
### adds genes as parents to polypeptide

# This will re-build the last column of the file
# according to the dictionaries created in those sections
def formColmn8(pPairList):
    colm8 = ""
    for key, value in pPairList.items():
        if colm8 != "":
            colm8 = colm8 + ";"
        colm8 = colm8 + key + "=" + value
    return colm8


hit_dict = {}  # create empty dictionary for ID match between transcripts and EST gene iDs
descrip_dict = {}  # create empty dictionary for polypeptide description

# original GFF from NCBI
gff = open("GCF_002906115.1_CorkOak1.0_genomic.gff", "r")
# text for the description field based on publications published before the article (2 columns: ID, description)
descrip = open("polypeptides_with_description.txt",
               "r")
# matching file between the mRNA IDs and the gene IDs from the previous CorkOakDB portal (2 columns: ID, description)
est = open("compList_hit.txt",
           "r")
file_out = open("CorkOakDB_genomic_Nov2020.gff", "w")


def getIDs():  # populates dictionary with key-value of transcript/mRNA ID-EST gene ID
    for line in est:
        line_l = line.strip().split()
        hit = line_l[0]
        genes = line_l[1]
        hit_dict[hit] = genes
    return hit_dict


def getdescrip():  # populates dictionary with key-value of polypeptide-description
    for line in descrip:
        line_l = line.strip().split("\t")
        polyp = line_l[0]
        desc = line_l[1]
        descrip_dict[polyp] = desc
    return descrip_dict


wGene = True  # flag for when the gene line has no mRNA associated with it
for line in gff:
    if line[0] == "#":  # prints all ## lines
        file_out.write(line)
    else:
        line_l = line.strip().split("\t")
        if line_l[2] == "mRNA":
            features_p = line_l[8]
            feature_l = features_p.strip('"').split(";")
            transcID = feature_l[0][7:]  # saves the ID of mRNA lines
            type = line_l[2]

            # runs function defined above
            # returns the dictionary w/ matches to EST portal IDS
            getIDs()

            # creates dictionary of the last column
            # fields split by ;
            # key-value by =
            attrmRNA = dict(item.split("=") for item in line_l[8].split(";"))
            attrGene["product"] = attrmRNA.get("product")
            file_out.write("\t".join(lineGene[:8]) + "\t" + formColmn8(attrGene) + ";Type=" + typeG + "\n")
            wGene = True

            line_l[2] = "transcript"
            transLine = line_l[0] + "\t" + line_l[1] + "\t" + line_l[2] + "\t" + line_l[3] + "\t" + line_l[4] + "\t" + \
                        line_l[5] + "\t" + line_l[6] + "\t" + line_l[7] + "\t" + line_l[
                            8] + ";Type=" + type + "\n"  # assembles transcript line
            if transcID in hit_dict:
                desLine = line_l[0] + "\t" + line_l[1] + "\t" + line_l[2] + "\t" + line_l[3] + "\t" + line_l[4] + "\t" + \
                          line_l[5] + "\t" + line_l[6] + "\t" + line_l[7] + "\t" + line_l[8] + ";" + "EST_IDs=" + \
                          hit_dict[transcID] + ";Type=" + type + "\n"  # assembles transcript line with EST IDs at the end
                file_out.write(desLine)  # prints line when there's a match to the EST IDs
            else:
                file_out.write(transLine)  # prints line when there's NOT a match to the EST IDs

        elif line_l[2] == "gene":
            features = line_l[8]
            feature_l = features.strip('"').split(";")
            geneID = feature_l[0][3:]  # saves gene ID
            typeG = line_l[2]

            # when genes have no mRNA lines
            # the flag will be set to False from this section
            # this bit will print the previous gene line when it reaches the new one
            if wGene is False:
                file_out.write(prevGene + ";Type=" + typeG + "\n")
            wGene = False
            attrGene = dict(item.split("=") for item in line_l[8].split(";"))
            line_l[8] = line_l[8] + ";Product="
            lineGene = line_l
            prevGene = line.rstrip("\n")

        elif line_l[2] == "CDS":
            features = line_l[8]
            feature_l = features.strip('"').split(";")
            cdsID = feature_l[0][7:]  # saves CDS ID

            # runs function defined above
            # returns the dictionary w/ descriptions
            getdescrip()

            attrCDS = dict(item.split("=") for item in line_l[8].split(";"))
            attrPolyp = attrCDS
            attrPolyp["Parent"] = attrPolyp.get("Parent") + "," + geneID  # adds gene ID as parent

            namePolyp = attrPolyp["Name"]

            if namePolyp in descrip_dict:
                attrPolyp["ID"] = "polypeptide-" + cdsID
                polyD_line = line_l[0] + "\t" + line_l[1] + "\t" + "polypeptide" + "\t" + line_l[3] + "\t" + line_l[
                    4] + "\t" + line_l[5] + "\t" + line_l[6] + "\t" + line_l[
                                 7] + "\t" + formColmn8(attrPolyp) + ";" + "Description=" + descrip_dict[
                                 namePolyp] + "\n"
                file_out.write(polyD_line)  # prints lines w/ descriptions

                attrCDS["Name"] = "cds-" + attrCDS["Name"]
                attrCDS["ID"] = attrCDS["Name"]
                file_out.write("\t".join(line_l[:8]) + "\t" + formColmn8(attrCDS) + "\n")  # prints CDS line
            else:
                attrPolyp["ID"] = "polypeptide-" + cdsID
                poly_line = line_l[0] + "\t" + line_l[1] + "\t" + "polypeptide" + "\t" + line_l[3] + "\t" + line_l[
                    4] + "\t" + line_l[5] + "\t" + line_l[6] + "\t" + line_l[
                                7] + "\t" + formColmn8(attrPolyp) + "\n"
                file_out.write(poly_line)  # prints lines w/o descriptions

                attrCDS["Name"] = "cds-" + attrCDS["Name"]
                attrCDS["ID"] = attrCDS["Name"]
                file_out.write("\t".join(line_l[:8]) + "\t" + formColmn8(attrCDS) + "\n")  # prints CDS line

        elif line_l[2] == "lnc_RNA" or line_l[2] == "rRNA" or line_l[2] == "snRNA" or line_l[2] == "snoRNA" or line_l[2] == "tRNA":
            type = line_l[2] # saves type (3rd column)
            line_l[2] = "transcript"
            RNALine = line_l[0] + "\t" + line_l[1] + "\t" + line_l[2] + "\t" + line_l[3] + "\t" + line_l[4] + "\t" + \
                        line_l[5] + "\t" + line_l[6] + "\t" + line_l[7] + "\t" + line_l[
                            8] + ";Type=" + type + "\n"  # assembles transcript line for all other types
            file_out.write(RNALine)

        elif line_l[2] == "pseudogene":
            type = line_l[2] # saves type (3rd column)
            line_l[2] = "gene"
            pseudoLine = line_l[0] + "\t" + line_l[1] + "\t" + line_l[2] + "\t" + line_l[3] + "\t" + line_l[4] + "\t" + \
                       line_l[5] + "\t" + line_l[6] + "\t" + line_l[7] + "\t" + line_l[
                           8] + ";Type=" + type + "\n" # assembles gene line for other type
            file_out.write(pseudoLine)

        elif line_l[2] == "transcript":
            features = line_l[8]
            feature_l = features.strip('"').split(";")
            type = feature_l[4][6:] # saves type (value of gbkey)
            miscLine = line_l[0] + "\t" + line_l[1] + "\t" + line_l[2] + "\t" + line_l[3] + "\t" + line_l[4] + "\t" + \
                         line_l[5] + "\t" + line_l[6] + "\t" + line_l[7] + "\t" + line_l[
                             8] + ";Type=" + type + "\n" # assembles transcript line for "true transcripts"
            file_out.write(miscLine)


        else:
            file_out.write(line)

file_out.close()
