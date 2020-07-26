import pandas as pd
import os
import csv
import processing

def MatchingKeys(diagnosis_csv, icd9_dx_csv, newfilename):
    #extract the code and description from the icd9_key file
    key = icd9_key[['dx_code','long_desc']]
    print(key)
    #Write a new dictionary linking codes to diseases
    dic = {}
    for x, dx_code, long_desc in key.itertuples():
        dic[dx_code] = long_desc
    #List of all the icd9 we see in diaganosis
    diagnosis = processing.padding_icd9(diagnosis_csv, 'icd9code');
    m = diagnosis.icd9code.unique()
    l = []
    #Iterate through the list of codes and add their respective long descriptions
    for icd9 in m:
        # code = str(icd9).split(", ")[0]
        code = icd9
        if(code in dic):
            l.append([code, dic[code]])
        else:
            print(code)
    #Write the CSV file
    with open(newfilename,'w', newline = '') as result_file:
        wr = csv.writer(result_file, delimiter = ',')
        for row in l:
            wr.writerow(row)

diagnosis = pd.read_csv(os.path.join(os.getcwd(), "diagnosis1.csv"))
icd9_key = pd.read_csv(os.path.join(os.getcwd(), "icd9_dx.csv"), encoding = 'latin1')
newfile = "diagnosis_hypokalemia1.csv"
MatchingKeys(diagnosis, icd9_key, newfile)