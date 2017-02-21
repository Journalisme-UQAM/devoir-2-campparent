# coding: utf-8

import csv

fichier = "concordia1.csv"
f1=open(fichier)


with open('concordia1.csv', 'rU') as truc:
  chose = csv.DictReader(truc)
  data = {}
  for colonne in chose:
    for header, value in colonne.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

longTitre = data['title']
diplome = data['thesis_degree_name']
nbPages = data['pages_aacr']
auteur = data['creators_name.given'] + data['creators_name.family']

print(longTitre,diplome,nbPages)
print(len(longTitre))

#for phrase in fichier:
    #print(diplome("{} de ".format(fichier)),auteur("{} compte ".format(fichier)),nbPages("{} de pages. Son titre est ".format(fichier)),longTitre)
    #print(len(longTitre))
    
