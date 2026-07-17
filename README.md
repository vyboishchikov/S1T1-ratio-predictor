# S1T1-ratio-predictor
A neural network for predicting *E*(*S*<sub>1</sub>)/*E*(*T*<sub>1</sub>) ratio for benzannulated biphenylenes. For test purposes only.

## Description

**S1T1-ratio-predictor** uses a trained dense neural network to predict the ratio of singlet to triplet excitation energies *E*(*S*<sub>1</sub>)/*E*(*T*<sub>1</sub>) for benzannulated biphenylenes.

**Author:** Sergei F. Vyboishchikov (Universitat de Girona, Spain)

**Date:** July 2026

## Requirements

The file `ModelData.pkl`, containing the model parameters, is required.

The following Python packages are required: `RDKit`, `NumPy`, `pickle`

## Usage

```S1T1-ratio-predictor smiles1 smiles2 ... ```

### Arguments

- `smiles1`, `smiles2`, ...: SMILES strings corresponding to for benzannulated biphenylenes

## How it works

The program:

1. Reads the SMILES strings of the solutes and the solvent name from the command line.
2. Converts the SMILES strings into count-based Morgan fingerprints using RDKit.
3. Applies the trained neural network.
4. Outputs the predicted *E*(*S*<sub>1</sub>)/*E*(*T*<sub>1</sub>) values.

## Bibliography

The paper is under consideration.
