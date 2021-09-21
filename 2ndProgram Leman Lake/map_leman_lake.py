import sys as sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
import random

indic1=0
indic2=1
valeur=int()
tableau=[]

f1 = open ('database_vecteur.txt','w')
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"19 " +"29 " +"0 "  +"0 "  +"0 "  +"21 " +"24 " +"28 " +"25 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"18 " +"19 " +"24 " +"24 " +"21 " +"20 " +"21 " +"26 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"17 " +"20 " +"20 " +"19 " +"24 " +"23 " +"22 " +"21 " +"23 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"28 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"18 " +"21 " +"20 " +"20 " +"19 " +"19 " +"19 " +"22 " +"22 " +"22 " +"22 " +"23 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"26 " +"26 " +"27 " +"24 " +"21 " +"28 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"20 " +"21 " +"22 " +"21 " +"22 " +"24 " +"23 " +"23 " +"22 " +"22 " +"21 " +"18 " +"19 " +"19 " +"21 " +"21 " +"22 " +"22 " +"23 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"25 " +"27 " +"26 " +"24 " +"24 " +"26 " +"28 " +"28 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"20 " +"20 " +"20 " +"20 " +"22 " +"24 " +"21 " +"22 " +"22 " +"22 " +"19 " +"18 " +"18 " +"19 " +"19 " +"20 " +"20 " +"21 " +"22 " +"22 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"24 " +"26 " +"24 " +"24 " +"26 " +"28 " +"26 " +"24 " +"24 " +"25 " +"25 " +"24 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"20 " +"19 " +"19 " +"19 " +"18 " +"19 " +"18 " +"20 " +"20 " +"20 " +"19 " +"18 " +"17 " +"17 " +"18 " +"19 " +"19 " +"19 " +"19 " +"22 " +"20 " +"24 " +"24 " +"24 " +"24 " +"24 " +"40 " +"40 " +"40 " +"24 " +"24 " +"24 " +"24 " +"24 " +"26 " +"24 " +"24 " +"27 " +"26 " +"26 " +"28 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"17 " +"20 " +"20 " +"18 " +"17 " +"20 " +"17 " +"22 " +"17 " +"18 " +"18 " +"17 " +"17 " +"15 " +"16 " +"19 " +"18 " +"18 " +"18 " +"20 " +"22 " +"22 " +"22 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"26 " +"24 " +"24 " +"26 " +"28 " +"28 " +"26 " +"29 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"21 " +"22 " +"17 " +"17 " +"17 " +"16 " +"19 " +"17 " +"18 " +"18 " +"19 " +"19 " +"17 " +"16 " +"11 " +"14 " +"19 " +"17 " +"17 " +"17 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"27 " +"28 " +"29 " +"24 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"20 " +"19 " +"18 " +"17 " +"16 " +"15 " +"17 " +"18 " +"17 " +"17 " +"18 " +"17 " +"16 " +"15 " +"8 "  +"8 "  +"16 " +"15 " +"16 " +"16 " +"40 " +"40 " +"2 "  +"6 "  +"8 "  +"8 "  +"8 "  +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"31 " +"29 " +"29 " +"27 " +"24 " +"24 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"20 " +"21 " +"18 " +"17 " +"16 " +"17 " +"16 " +"17 " +"17 " +"21 " +"15 " +"17 " +"16 " +"14 " +"40 " +"7 "  +"5 "  +"12 " +"12 " +"14 " +"10 " +"8 "  +"7 "  +"3 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"9 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"40 " +"40 " +"40 " +"40 " +"40 " +"40 " +"2 "  +"1 "  +"31 " +"31 " +"31 " +"28 " +"27 " +"24 " +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"18 " +"20 " +"17 " +"16 " +"15 " +"16 " +"16 " +"16 " +"17 " +"19 " +"14 " +"15 " +"11 " +"10 " +"3 "  +"4 "  +"0 "  +"8 "  +"9 "  +"10 " +"8 "  +"8 "  +"7 "  +"8 "  +"6 "  +"7 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"3 "  +"2 "  +"31 " +"29 " +"28 " +"27 " +"24 " +"0 "+"\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"20 " +"17 " +"21 " +"17 " +"28 " +"17 " +"12 " +"13 " +"14 " +"17 " +"16 " +"16 " +"15 " +"15 " +"13 " +"8 "  +"6 "  +"1 "  +"0 "  +"0 "  +"7 "  +"9 "  +"10 " +"8 "  +"7 "  +"8 "  +"5 "  +"5 "  +"5 "  +"5 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"4 "  +"3 "  +"2 "  +"1 "  +"31 " +"30 " +"28 " +"24 " +"0 "+"\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"20 " +"17 " +"15 " +"13 " +"14 " +"7 "  +"8 "  +"7 "  +"9 "  +"12 " +"16 " +"14 " +"14 " +"14 " +"10 " +"8 "  +"6 "  +"7 "  +"3 "  +"0 "  +"0 "  +"0 "  +"0 "  +"8 "  +"6 "  +"5 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"7 "  +"9 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"8 "  +"1 "  +"2 "  +"3 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"20 " +"20 " +"16 " +"12 " +"9 "  +"5 "  +"5 "  +"7 "  +"0 "  +"0 "  +"12 " +"12 " +"14 " +"11 " +"9 "  +"8 "  +"6 "  +"4 "  +"5 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"9 "  +"8 "  +"7 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"20 " +"19 " +"17 " +"9 "  +"3 "  +"6 "  +"0 "  +"0 "  +"0 "  +"0 "  +"8 "  +"11 " +"11 " +"12 " +"4 "  +"9 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"18 " +"18 " +"20 " +"2 "  +"2 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"8 "  +"9 "  +"4 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"20 " +"17 " +"22 " +"19 " +"1 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"19 " +"23 " +"21 " +"18 " +"1 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"17 " +"24 " +"21 " +"17 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"20 " +"16 " +"26 " +"20 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"19 " +"19 " +"22 " +"18 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"17 " +"26 " +"19 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"20 " +"17 " +"22 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"18 " +"22 " +"17 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"16 " +"28 " +"20 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"19 " +"22 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"14 " +"22 " +"19 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"15 " +"23 " +"17 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"16 " +"19 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"20 " +"17 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"20 " +"25 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"20 " +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")
f1.write ("0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "  +"0 "+ "\n")

f1.close()

image=np.zeros((64*9,36*9,4),dtype=np.uint8)

def prt (s):
    """ Writes and flushes without delay a text in the console"""
    sys.stdout.write(s)
    sys.stdout.flush()

def generation (image,tableau):
    im3=np.copy(image)
    for k in range(len(tableau)):
        for i in range(len(tableau[0])):
            if int(tableau[k][i])!=0:
                for j in range(0,9,3):
                    for l in range(0,9,3):
                        im3[i*9-1+j,k*9-1+l]=np.array([135,135,135,135])
    return(im3)

def mouvement (tableau,h2,i2,liste,lastp):
    deplacement=[(0,0),(-4,1),(-4,2),(-4,3),(-4,4),(-3,4),(-2,4),(-1,4),(0,4),(1,4),(2,4),(3,4),(4,4),(4,3),(4,2),(4,1),(4,0),(4,-1),(4,-2),(4,-3),(4,-4),(3,-4),(2,-4),(1,-4),(0,-4),(-1,-4),(-2,-4),(-3,-4),(-4,-4),(-4,-3),(-4,-2),(-4,-1)]
    if int(tableau[h2//9][i2//9])==0:
        fin="Oui"
        im2[i2,h2]=np.array([255,0,0,135])
    else:
        if int(tableau[h2//9][i2//9])==40:
            mvmt=lastp
            fin="Non"
        else:
            mvmt=deplacement[int(tableau[h2//9][i2//9])]
            lastp=mvmt
            fin="Non"
        vit=random.randint(0,2)
        h2=floor(h2+mvmt[0]*vit)
        i2=floor(i2+mvmt[1]*vit)

    return(h2,i2,lastp,fin)

def lancement (hauteur,largeur,im2,tableau,liste,nb_couleur):
    lastp=(0,0)
    couleur=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    compteur=0
    liste_coord=[[hauteur,largeur]]
    while hauteur!=0 and largeur!=0 and hauteur!=36*9-1 and i2 !=63*9-1 and compteur < 500 :
        hauteur,largeur,lastp,fin=mouvement(tableau,hauteur,largeur,liste,lastp)
        if fin=="Oui":
            data_end.append([hauteur//9,largeur//9,compteur])
            compteur=30000
            #im6[largeur,hauteur]=np.array([couleur[0],couleur[1],couleur[2],135])

        else:
            if hauteur<0:
                hauteur=0
            elif hauteur>36*9-1:
                hauteur=36*9-1
            if largeur<0:
                largeur=0
            elif largeur>63*9-1:
                largeur=63*9-1
                
            im2[largeur,hauteur]=np.array([couleur[0],couleur[1],couleur[2],135])
            
            if nb_couleur==indic1:
                im7[largeur,hauteur]=np.array([255,255,255,135])
                
            if nb_couleur==indic2:
                im8[largeur,hauteur]=np.array([255,255,255,135])
                
            if compteur==50:
                im4[largeur,hauteur]=np.array([couleur[0],couleur[1],couleur[2],135])
                
            if compteur==0:
                im5[largeur,hauteur]=np.array([couleur[0],couleur[1],couleur[2],135])

            compteur=compteur+1
            liste_coord.append([largeur,hauteur])
            if liste_coord[compteur]==liste_coord[compteur-1]:
                hauteur=hauteur+random.randint(-2,2)
                largeur=largeur+random.randint(-2,2)
    if compteur<2000:
        data_end.append([hauteur//9,largeur//9,compteur])

f2 = open ('database_vecteur.txt','r')

liste=f2.readlines()
im1=generation(image,tableau)

tableau=[]

for k in range (len(liste)):
    a=liste[k].split()
    tableau.append(a)

liste_coord=[]
for k in range(1,len(tableau)-1):
    for i in range(1,len(tableau[0])-1):
        
        if int(tableau[k][i])!=0:
            liste_coord.append((k,i))
            for j in range(0,9):
                    for l in range(0,9):
                        im1[i*9-1+j,k*9-1+l]=np.array([29,51,74,135])
                        
        elif int(tableau[k+1][i-1])!=0 or int(tableau[k+1][i+1])!=0 or int(tableau[k-1][i+1])!=0 or int(tableau[k-1][i-1])!=0:
            for j in range(0,9):
                    for l in range(0,9):
                        im1[i*9-1+j,k*9-1+l]=np.array([174,137,100,135])
        for j in range(0,9):
                for l in range(0,9):
                    im1[9-1+j,34*9-1+l]=np.array([29,51,74,135])


im2=np.copy(im1)
im4=np.copy(im2)
im5=np.copy(im2)
im6=np.copy(im2)
im7=np.copy(im2)
im8=np.copy(im2)

nb_repet=int(input("Combien voulez vous lancer de particules ? "))

data_end=[]

chargement=[[int(np.around(0.1*nb_repet)),9],[int(np.around(0.2*nb_repet)),8],[int(np.around(0.3*nb_repet)),7],[int(np.around(0.4*nb_repet)),6],[int(np.around(0.5*nb_repet)),5],[int(np.around(0.6*nb_repet)),4],[int(np.around(0.7*nb_repet)),3],[int(np.around(0.8*nb_repet)),2],[int(np.around(0.9*nb_repet)),1],[nb_repet,0]]
compte=0
print(10)

for k in range(nb_repet):
    if k==chargement[compte][0]:
        print(chargement[compte][1])
        compte=compte+1
    nbcoord=liste_coord[random.randint(0,len(liste_coord)-1)]
    i2=nbcoord[1]*9+4
    h2=nbcoord[0]*9+4
    lancement(h2,i2,im2,tableau,liste,k)
    im2[i2,h2]=np.array([0,255,0,135])
    if k==indic1:
        im7[i2,h2]=np.array([0,255,0,135])
        if data_end[k][2]<40:
            indic1=indic1+1
            im7=np.copy(im1)
    if k==indic2:
        if data_end[k][0]>31 and data_end[k][1]<2 and data_end[k][2]>10:
            im8[i2,h2]=np.array([0,255,0,135])
        else:
            indic2=indic2+1
            im8=np.copy(im1)

        

#Traitement données:
data_end.sort()
part_riv=[]
data_lac=[]
data_ech_list=[]
data_ech=[]
coord_fin=[]
tvoyage=0
voyageinf=0
for k in range(len(data_end)):
    if data_end[k][0]>31 and data_end[k][1]<2:
        part_riv.append(data_end[k])
    else:
        data_lac.append(data_end[k])
        if data_end[k][2]>400:
            voyageinf=voyageinf+1
        else:
            data_ech_list.append(data_end[k])
            tvoyage=tvoyage+data_end[k][2]
        if ([data_end[k][0],data_end[k][1]] not in coord_fin):
            coord_fin.append([data_end[k][0],data_end[k][1]])

compt=-1
nb_ech=[]
fin_ech=[]
for k in range(len(data_ech_list)):
    if [data_ech_list[k][0],data_ech_list[k][1]] in data_ech:
       nb_ech[compt]=nb_ech[compt]+1
    else:
        compt=compt+1
        data_ech.append([data_ech_list[k][0],data_ech_list[k][1]])
        nb_ech.append(1)

for k in range(len(data_ech)):
    fin_ech.append([data_ech[k][0],data_ech[k][1],nb_ech[k]/len(data_ech_list)])

for k in range(len(data_ech)):
    for j in range(0,9):
        for l in range(0,9):
            porcent=1-((fin_ech[k][2]))/(max(nb_ech)/len(data_ech_list))
            im6[fin_ech[k][1]*9-1+j,fin_ech[k][0]*9-1+l]=np.array([255,135*porcent,135*porcent,135])

print(round((len(part_riv)/nb_repet)*100),"% des particules sont dans la rivière.")
print(round(tvoyage//len(data_lac)),"déplacements sont effectués par les particules qui s'echouent avant",400,"deplacements")
print(round((voyageinf/nb_repet)*100),"% des particules sont encore en voyage après",400,"déplacements.")

rev2=np.zeros((36*9,64*9,4),dtype=np.uint8)
rev4=np.zeros((36*9,64*9,4),dtype=np.uint8)
rev5=np.zeros((36*9,64*9,4),dtype=np.uint8)
rev6=np.zeros((36*9,64*9,4),dtype=np.uint8)
rev7=np.zeros((36*9,64*9,4),dtype=np.uint8)
rev8=np.zeros((36*9,64*9,4),dtype=np.uint8)

for k in range(36*9):
    for l in range(64*9):
        rev2[k][l]=im2[l][k]
        rev4[k][l]=im4[l][k]
        rev5[k][l]=im5[l][k]
        rev6[k][l]=im6[l][k]
        rev7[k][l]=im7[l][k]
        rev8[k][l]=im8[l][k]


panorama=np.zeros((36*9*3,64*9*2,4),dtype=np.uint8)
for k in range(36*9):
    for l in range(64*9):
        panorama[k][l]=rev5[k][l]
        panorama[k][l+64*9]=rev6[k][l]
        panorama[k+36*9][l]=rev4[k][l]
        panorama[k+36*9][l+64*9]=rev2[k][l]
        panorama[k+2*36*9][l]=rev7[k][l]
        panorama[k+2*36*9][l+64*9]=rev8[k][l]


plt.imsave('Result.bmp',panorama)
##plt.imsave('r_superposition_multi.bmp',rev2)
##plt.imsave('r_instant50.bmp',rev4)
##plt.imsave('r_instant0.bmp',rev5)
##plt.imsave('r_instantfinal.bmp',rev6)
##plt.imsave('r_superposition_solo1.bmp',rev7)
##plt.imsave('r_superposition_solo2.bmp',rev8)
