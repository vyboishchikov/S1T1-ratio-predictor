'''
A neural network for predicting E(S1)/E(T1) ratio for benzannulated biphenylenes
Author: Sergei F. Vyboishchikov
Universitat de Girona, July 2026
The program is used from the command line:
S1T1-ratio-predict.py smiles1 smiles2 ... 
Required modules: RDKit, Numpy, and Pickle
For test purposes only
'''

import sys, pickle, numpy as np
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator

if len(sys.argv) <= 1:
   print("Usage: S1T1-ratio-predict.py smiles1 smiles2 ...")
   sys.exit()

Smiles = sys.argv[1:]

ModelData = "ModelData.pkl"
try:
   mask,model,nCounts,radius = pickle.load(open(ModelData,"rb"))
except:
   print('Model file "'+ModelData+'" does not exist, cannot be opened, or has an incorrect format')
   sys.exit()

NData = len(Smiles)
MorganMatrix = np.zeros((NData,nCounts),dtype='int')
MistakeVector = np.zeros(NData,dtype='int')
NotBiphenyleneVector = np.zeros(NData,dtype='int')
biphenylene_fragment = Chem.MolFromSmarts('c1ccc-2c(c1)-c3c2cccc3')
for i, smi in enumerate(Smiles):
  try:
  	mol = Chem.MolFromSmiles(smi)
  	if len(mol.GetSubstructMatches(biphenylene_fragment))==0:
  		NotBiphenyleneVector[i] = 1
  	MorganMatrix[i] = rdFingerprintGenerator.GetMorganGenerator(radius=radius,fpSize=nCounts).GetCountFingerprintAsNumPy(mol)
  except:
  	MistakeVector[i] = 1

Predictions = model.predict(MorganMatrix[:,mask])

if NData==1:
	print("Predicted E(S1)/E(T1) ratio:")
else:
	print("Predicted E(S1)/E(T1) ratios:")
for i,(smi,prediction) in enumerate(zip(Smiles, Predictions)):
   if MistakeVector[i]:
   	print(smi+":\tMistake in SMILES")
   elif NotBiphenyleneVector[i]:
   	print(smi+":\t%5.2f  Warning: not a biphenylene"%prediction)
   else:
   	print(smi+":\t%5.2f"%prediction)
