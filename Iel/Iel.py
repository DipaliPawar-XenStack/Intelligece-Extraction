import csv
def uOpen():
        a= input('Enter the name of your input file: ')
        global y
        y= input("Enter the name of column to split: ")
    
        with open(a,'r') as csv_file:
            csv_reader= csv.DictReader(csv_file)
        
            for line in csv_reader:
                global b
                b=input('Enter new name of csv File: ') 
                with open(b,'w') as new_file:
                    csv_writer = csv.writer(new_file, delimiter='\t')
                    for line in csv_reader:
                        csv_writer.writerow(line[y])


import pandas as pd        
def split():
    b=input('Enter the csv File')
    r=pd.read_csv(b,error_bad_lines=False)
    r.columns=[y]
    r.dropna(inplace=True)
    c=input("Enter the input Symbol:")
    new = r[y].str.split(c, n = 4, expand = True)
    d=int(input('Enter number of column='))
    i=0
    for i in range(d):
        r[i]=new[i]
        i+=1
   
    r.drop(columns =[y], inplace = True) 
    new= new.fillna(0)
    c=input('Enter the Output file name:')
    new.to_csv(c)