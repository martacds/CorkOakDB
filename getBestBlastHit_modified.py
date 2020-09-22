file = open("rnaSEQ_QSgeneFNA.txt", "r")
file_out = open("uniqXM.txt", "w")
file_out.write('query' + '\t' + 'hit' + '\t' + 'evalue' + '\t' + 'bit_score' + '\n')

id_list = []
uniqueID = ''
for line in file:
    line = line.strip().split()
    gene = line[0]
    hit = line[1]
    queryID = hit
    evalue = line[len(line) - 2]
    bit_score = line[len(line) - 1]
    # print hit
    if queryID != uniqueID:
        # print queryID + '\t' + uniqueID
        file_out.write(gene + '\t' + queryID + '\t' + evalue + '\t' + bit_score + '\n')
        uniqueID = queryID
        # print uniqueID

file.close()
file_out.close()

file = open("uniqXM.txt", "r")
file_out = open("twinXM.txt", "w")
file_out.write('query' + '\t' + 'hit' + '\t' + 'evalue' + '\t' + 'bit_score' + '\n')

id_list = []
twinID = ''
eOLD = ''
for line in file:
    line = line.strip().split()
    gene = line[0]
    twinGene = gene
    hit = line[1]
    evalue = line[len(line) - 2]
    eNEW = evalue
    bit_score = line[len(line) - 1]
    if twinID == twinGene:
        if eOLD == eNEW:
            file_out.write(gene + '\t' + hit + '\t' + evalue + '\t' + bit_score + '\n')
            eOLD = evalue
            twinID = gene
        else:
            pass
    elif twinID != twinGene:
        file_out.write(gene + '\t' + hit + '\t' + evalue + '\t' + bit_score + '\n')
        eOLD = evalue
        twinID = gene

file.close()
file_out.close()
