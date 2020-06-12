file = open("CorkOak1.0_protein.faa.xml", "r")
gff = open("Genomic_addProduct_changeCDS_4.gff", "r")
file_out = open("CorkOak_gene_2020apr.xml", "w")

def formColmn8(pPairList):
    colm8 = ""
    for key, value in pPairList.items():
        if colm8 != "":
            colm8 = colm8 + ";"
        colm8 = colm8 + key + "=" + value
    return colm8

def gene():
    for line in gff:

        line_l = line.strip().split("\t")

        if len(line_l) == 9:
            if line_l[2] == "gene":
                attrGene = dict(item.split("=") for item in line_l[8].split(";"))
                # print(attrGene["Name"])
                #file_out.write(attrGene["Name"] + "\n")
                return attrGene["ID"]
    else:
        pass


def poly():
    for line in gff:

        line_l = line.strip().split("\t")
        if len(line_l) == 9:
            if line_l[2] == "polypeptide":
                attrPoly = dict(item.split("=") for item in line_l[8].split(";"))
                # print(attrPoly["Name"])
                #file_out.write(attrPoly["Name"] + "\n")
                return attrPoly["Name"]

    else:
        pass


def changeXP():
    for line in file:
        if 'xref id=' in line:
            #print(line)
            #file_out.write(gene() + "\t")
            #file_out.write(poly() + "\n")
            line_XP = line.strip().split(" ")
            attrXP = dict(item.split("=") for item in line_XP[1].split(" "))
            #print(attrXP["id"])
            attrXP["id"] = "\"" + gene() + "\""
            #print(attrXP["id"])
            line_new = line_XP[0] + " " + formColmn8(attrXP) + "/>" + "\n"
            print(line_new)
            file_out.write(line_new)
            #return attrXP["id"]

        else:
            file_out.write(line)

changeXP()

file_out.close()
