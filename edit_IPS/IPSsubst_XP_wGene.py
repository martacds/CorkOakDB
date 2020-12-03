## script to change the InterProScan file from polypeptide IDs to gene IDs
## there's a hiccup in the first section
### a blank line is created at the beginning
### and it interferes w/ the rest of the script

# gff = open("CorkOakDB_genomic_Nov2020.gff", "r")
# file_match = open("genePolypeptide_match.txt", "w")
# 
# prevID = ""
# for line in gff:
#     if line[0] == "#":
#         pass
#     else:
#         line_l = line.strip().split("\t")
#         if line_l[2] == "gene":
#             features = line_l[8]
#             feature_l = features.strip('"').split(";")
#             geneID = feature_l[0][3:] # gets gene ID
#             file_match.write("\n" + geneID + "\t")
#     # this creates a blank line at the beginning of the file that has to be removed for the rest to work
# 
#         elif line_l[2] == "polypeptide":
#             features = line_l[8]
#             feature_l = features.strip('"').split(";")
#             polypID = feature_l[0][15:] # gets polypeptide ID
#             if polypID == prevID:
#                 pass # there are several lines w/ the same polypeptide (different coordinates)
#             else:
#                 prevID = polypID # saves ID for the if above
#                 file_match.write(polypID)
# 
#         else:
#             pass
# file_match.close()


ips = open("CorkOak1.0_protein.faa.xml", "r")
file_match2 = open("genePolypeptide_match.txt", "r")
file_final = open("CorkOak1.0_gene.xml", "w")

match = {} # creates empty dictionary for the match between gene and polypeptide
def getMatch():
    for line in file_match2:
        column = line.split("\t")
        if column[1] != "": # some genes don't have polypeptides
            gene = column[0]
            polypeptide = column[1][:-1] # removes new line char
            match[polypeptide] = gene # creates dictionary
    return match


for line in ips:
    if 'xref id=' in line:
        line_ips = line.strip().split(" ")

        getMatch()
        polypName_asp = dict(item.split("=") for item in line_ips[1].split(" "))
        polypName = polypName_asp["id"][1:15] # value for ID includes ""s

        if polypName in match:
            geneID = match.get(polypName) # gets gene ID based on match w/ dict based on polypeptide ID
            geneLine = "        <xref id=\"" + geneID + "\" name=\"" + geneID[5:] + "\"/>" + "\n"
            file_final.write(geneLine)

    else:
        file_final.write(line)

file_match2.close()
file_final.close()
