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

#La formule n'est pas complète mais c'est le mieux que j'ai su faire avec l'aide de l'ami Google. Avec print(longTitre,diplome,nbPages) et
#print(len(longTitre)), je n'obtiens que les variables qui ne sont pas en relation entre elles, comme elles l'auraient été dans la phrase
#demandée. J'ai essayé de les mettre dans une phrase, mais celle-ci n'as pas fonctionné malgré mes différents essais. Bref.


    
