# adds the gene as a parent to the CDS line
# creates a new line: polypeptide
# adds the info from the CDS line to the polypeptide line
# adds description tag to the end of features: gene, mRNA, CDS, polypeptide
# adds the info from the product field to the gene line

def formColmn8(pPairList):
    colm8 = ""
    for key, value in pPairList.items():
        if colm8 != "":
            colm8 = colm8 + ";"
        colm8 = colm8 + key + "=" + value
    return colm8

file = open("GCF_002906115.1_CorkOak1.0_genomic.gff", "r")
file_out = open("Genomic_addPolypeptide_addParent_1.gff", "w")
for line in file:
    if line[0] == "#":
        file_out.write(line)
    else:
        line_l = line.strip().split("\t")
        if line_l[2] == "gene":
            features = line_l[8]
            feature_l = features.strip('"').split(";")
            geneID = feature_l[0][3:]
            file_out.write(line)

        elif line_l[2] == "CDS":
            features = line_l[8]
            feature_l = features.strip('"').split(";")
            cdsID = feature_l[0][7:]

            attrCDS = dict(item.split("=") for item in line_l[8].split(";"))
            attrCDS["Parent"] = attrCDS.get("Parent") + "," + geneID
            file_out.write("\t".join(line_l[:8]) + "\t" + formColmn8(attrCDS) + "\n")

            poly_line = line_l[0] + "\t" + line_l[1] + "\t" + "polypeptide" + "\t" + line_l[3] + "\t" + line_l[
                4] + "\t" + line_l[5] + "\t" + line_l[6] + "\t" + line_l[
                            7] + "\t" + "ID=polypeptide-" + cdsID + "\n"
            file_out.write(poly_line)
        else:
            file_out.write(line)

file_out.close()

file = open("Genomic_addPolypeptide_addParent_1.gff", "r")
file_out = open("Genomic_addCDStoPolypeptide_2.gff", "w")
for line in file:
    if line[0] == "#":
        file_out.write(line)
    else:
        line_l = line.strip().split("\t")
        if line_l[2] == "CDS":
            features = line_l[8][22:]

            file_out.write(line)

        elif line_l[2] == "polypeptide":
            features_p = line_l[8]
            feature_l = features_p.strip('"').split(";")
            polyID = feature_l[0]
            newLine = line_l[0] + "\t" + line_l[1] + "\t" + line_l[2] + "\t" + line_l[3] + "\t" + line_l[4] + "\t" + \
                      line_l[5] + "\t" + line_l[6] + "\t" + line_l[7] + "\t" + polyID + ";" + features + "\n"
            file_out.write(newLine)
        else:
            file_out.write(line)
file_out.close()

file = open("Genomic_addCDStoPolypeptide_2.gff", "r")
file_out = open("Genomic_addDescription_3.gff", "w")
for line in file:
    if line[0] == "#":
        file_out.write(line)
    else:
        line_l = line.strip().split("\t")
        if line_l[2] == "gene" or line_l[2] == "CDS" or line_l[2] == "mRNA" or line_l[2] == "polypeptide":
            desLine = line_l[0] + "\t" + line_l[1] + "\t" + line_l[2] + "\t" + line_l[3] + "\t" + line_l[4] + "\t" + \
                      line_l[5] + "\t" + line_l[6] + "\t" + line_l[7] + "\t" + line_l[8] + ";" + "Description=..." + \
                      "\n"
            file_out.write(desLine)
        else:
            file_out.write(line)
file_out.close()


file = open("Genomic_addDescription_3.gff", "r")
file_out = open("Genomic_addProduct_changeCDS_4.gff", "w")

wGene = True
for line in file:

    line_l = line.strip().split("\t")

    #wGene = True
    if len(line_l) == 9:
        if line_l[2] == "gene":
            if wGene is False:
                file_out.write(prevGene)
            wGene = False
            attrGene = dict(item.split("=") for item in line_l[8].split(";"))
            line_l[8] = line_l[8] + ";Product="
            lineGene = line_l
            prevGene = line
        elif line_l[2] == "mRNA":
            attrmRNA = dict(item.split("=") for item in line_l[8].split(";"))
            attrGene["Product"] = attrmRNA.get("product")
            file_out.write("\t".join(lineGene[:8]) + "\t" + formColmn8(attrGene) + "\n")
            wGene = True
            file_out.write(line)
        elif line_l[2] == "CDS":
            attrCDS = dict(item.split("=") for item in line_l[8].split(";"))
            attrCDS["Name"] = "cds-" + attrCDS.get("Name")
            file_out.write("\t".join(line_l[:8]) + "\t" + formColmn8(attrCDS) + "\n")
        else:
            file_out.write(line)
    else:
        file_out.write(line)

file_out.close()
