before = open("CorkOak_genomic_edited2020_v2.gff", "r")
file = open("compList.txt", "r")
file_out = open("CorkOak_genomic_edited2020_v3.gff", "w")

data_dict = {}


def getIDs():
    for line in file:
        line_l = line.strip().split()
        hit = line_l[0]
        genes = line_l[1]
        data_dict[hit] = genes
        # matchIDs = dict(item.split() for item in line.split("\n"))
        # print(matchIDs)
    return data_dict


for line in before:
    if line[0] == "#":
        file_out.write(line)
    else:
        line_l = line.strip().split("\t")
        if line_l[2] == "transcript":
            features_p = line_l[8]
            feature_l = features_p.strip('"').split(";")
            transcID = feature_l[0][7:]

            getIDs()
            # print(data_dict[transcID])
            if transcID in data_dict:
                desLine = line_l[0] + "\t" + line_l[1] + "\t" + line_l[2] + "\t" + line_l[3] + "\t" + line_l[4] + "\t" + \
                          line_l[5] + "\t" + line_l[6] + "\t" + line_l[7] + "\t" + line_l[8] + ";" + "oldID=" + \
                          data_dict[transcID] + "\n"
                file_out.write(desLine)
            else:
                file_out.write(line)
        else:
            file_out.write(line)

file_out.close()
