# -*- coding: utf-8 -*-

from rdkit import Chem
import pandas as pd


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


# load data
path = "datasets/mergedData2.csv"

df = pd.read_csv(path)

# empty df for results
aug = pd.DataFrame(columns=['smiles', 'Class'])
rm = []

# augment
[augmentSMILES(smiles, label) for smiles, label in zip(df['smiles'], df['Class'])]

# delete those 11
for i in rm:
    df = df.drop(df[df['smiles'] == i].index, axis=0)

# append to canonical
df = df.append(aug, ignore_index=True)

# results
df.to_csv("datasets/augmented.csv")
