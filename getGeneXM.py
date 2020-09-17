file = open("GCF_002906115.1_CorkOak1.0_genomic.gff", "r")
file_out = open("geneXM.txt", "w")

for line in file:
    for line in file:
        if line[0] == "#":
            pass
        else:
            line_l = line.strip().split("\t")
            if line_l[2] == "gene":
                features = line_l[8]
                feature_l = features.strip('"').split(";")
                geneID = feature_l[0][3:]
                file_out.write("\n" + geneID + "\t")

            elif line_l[2] == "mRNA":
                features = line_l[8]
                feature_l = features.strip('"').split(";")
                mrnaID = feature_l[0][7:]
                file_out.write(mrnaID + ", ")

            # elif line_l[2] == "CDS":
            #     features = line_l[8]
            #     feature_l = features.strip('"').split(";")
            #     cdsID = feature_l[0][7:]
            #     file_out.write(cdsID + "\t")

            else:
                pass

file_out.close()
