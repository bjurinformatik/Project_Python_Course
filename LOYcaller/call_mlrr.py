#Script to call LOY
#Written to work for UK Biobank array data

#Import modules
import pandas as pd
import numpy as np

class call_loy:

    #Initiate class by reading files containing log R ratio values for chr X and Y, as well as a fam file to get individual id and reported sex
    def __init__(self, lrry_file, lrrx_file, fam_file):
        self.lrry = pd.read_csv(lrry_file, header=None, sep=' ', na_values='NA')
        self.lrrx = pd.read_csv(lrrx_file, header=None, sep=' ', na_values='NA')
        self.fam = pd.read_csv(fam_file, header=None, sep=' ')

    #Calculate the median log R ratio value for chr X and Y
    def calculate_mlrr(self):
        mlrry = self.lrry.median(axis=0, skipna=True)
        mlrrx = self.lrrx.median(axis=0, skipna=True)
    #Concatenate the output with the fam file and filter out individuals with chromosomal abberations   
        result = pd.concat([self.fam.loc[:,[1,4]], mlrry, mlrrx], axis=1)
        result.columns = ['id', 'sex', 'mlrry', 'mlrrx']
        male_mlrr = result.loc[(result['sex'] == 1) & (result['mlrry']<0.23) & (result['mlrrx']< -0.23)]
        return male_mlrr

    def save_output(self, output_file):
        male_mlrr = self.calculate_mlrr()
        male_mlrr.to_csv(output_file, index=False, sep='\t')
