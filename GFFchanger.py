file = open("GCF_002906115.1_CorkOak1.0_genomic.gff", "r")
file_out = open("GCF_002906115.1_CorkOak1.0_genomicNew.gff", "w")
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
            #print features

            feature_l = features.strip('"').split(";")
            # if "parent" in feature_l

            #parentCDS = feature_l[1][7:]
            feature_l[1] = "Parent="+geneID
            feature_l_start = "\t".join(line_l[:8])
            print feature_l_start
            feature_l_end = ";".join(feature_l)

            newline = feature_l_start + "\t" + feature_l_end + "\n"
            file_out.write(newline)
        else:
            file_out.write(line)

file_out.close()
