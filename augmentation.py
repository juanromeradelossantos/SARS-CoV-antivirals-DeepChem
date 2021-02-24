# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:17:26 2021

@author: juanr
"""

from rdkit import Chem
import pandas as pd


# load data
path = "C:/Users/juanr/Documents/Máster Bioinformatica UDC/3 cuatrimestre/TFM/Datos adicionales 2/mergedData2.csv"

df = pd.read_csv(path)

# empty df for results
aug = pd.DataFrame(columns=['smiles', 'Class'])
rm = []
def augmentSMILES(smiles, label):
    global aug
    global rm
    for _ in range(10):
        try:
            mol = Chem.MolFromSmiles(smiles)
            smi = Chem.MolToSmiles(mol, doRandom=True)
            aug = aug.append({'smiles':smi, 'Class':label}, ignore_index=True)
        except:
            rm.append(smiles)
            break  # 11 errors with doRandom=True
    return aug


# augment
_ = [augmentSMILES(smiles, label) for smiles, label in zip(df['smiles'], df['Class'])]

# delete those 11
for i in rm:
    df = df.drop(df[df['smiles'] == i].index, axis=0)

# append to canonical
df = df.append(aug, ignore_index=True)

# results
df.to_csv("C:/Users/juanr/Documents/Máster Bioinformatica UDC/3 cuatrimestre/TFM/augmented.csv")
