# -*- coding: utf-8 -*-

from pylab import randint
import xlrd, re

def rand_grp(names, grp_size):
    #Funksjon som tar inn en liste med names og en int som beskriver gruppestørrelse,
    #og lager tilfeldige grupper av den størrelsen. Hvis det ikke går opp
    #blir de resterende plassert i grupper (starter på gruppe 1).

    grp_list = []
    num_grps = len(names) // grp_size
    rest_ppl = len(names) % grp_size
    
    while len(names) >= grp_size:       #Lager nye grupper med grp_size tilfeldige elementer fra names
        new_grp = []
        for i in range(grp_size):
            new_grp.append(names.pop(randint(len(names))))
        grp_list.append(new_grp)
        
    
    for i in range(rest_ppl):           #Fyller inn de resterende personene
        grp_list[i % num_grps].append(names.pop(0))

    return grp_list
    
def print_grp(grp_list):
    #Skrive ut gruppelistene
    i = 1
    for grp in grp_list:
        print(f"Gruppe {i}: {grp}")
        i += 1
        
def print_grp_txt(grp_list):
    f = open("Grupper.txt", "w")
    i = 1
    for grp in grp_list:
        f.write(f"Gruppe {i}: ")
        for name in grp:
            if name == grp[-2]:
                f.write(f"{name} ")
            elif name == grp[-1]:
                f.write(f"og {name}.\n")
            else:
                f.write(f"{name}, ")
        i += 1
    f.close()
        
def read_name_txt(filename): #Henter inn første element fra hver rad i en nameseliste
    names = []
    with open(filename + ".txt",'r') as namelist:
        for line in namelist:
            names.append(line.split(None, 1)[0])

    return names

def read_name_xls(filename): #Henter inn første kolonne i excel-arket, gitt 1ST? i 3. kolonne
    names = []    
    workbook = xlrd.open_workbook(filename + ".xls")
    worksheet = workbook.sheet_by_name('Students')
    num_rows = worksheet.nrows - 1

    for i in range(num_rows):
        klasse = worksheet.cell(i+1,2).value
        if re.match("1ST?", klasse):
            names.append(worksheet.cell(i+1,0).value)
            
    return names
    

#elever_eirik = read_name_txt("1televerEirik")
#elever_eirik = read_name_xls("allemineelever")
elever_eirik = ["Frida", "Rolf Otto", "David", "Alexander", "Elver", "Sigurd", "Ludvig",
        "Vemund", "Jacob", "Maiken", "Sivert", "Sjur", "Alicja", "Ingeborg", 
        "Aurora", "Marius", "Storm", "Solange", "Tilde", "Karen", "William"]
elever_monica = ["Niki", "Sara", "Eline", "Tuva", "Theodor", "Dennis", "Helene", "Martin",
                 "Anoop", "Nora", "Jade",  "Stine Lise", "Syver"]
grp_size = 4
names = elever_eirik + elever_monica

print_grp_txt(rand_grp(names,grp_size))
