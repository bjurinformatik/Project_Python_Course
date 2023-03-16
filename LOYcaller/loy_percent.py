#Script to calculate percentage of LOY from mLRRY values

import numpy as np
import pandas as pd 

class mLRRYtoPer:

    def __init__(self, male_mlrr):
        self.mlrr = pd.read_csv("male_mlrr.txt", header=0, sep="\t")
        self.mlrry = self.mlrr.loc[:,'mlrry']
        
    def loy_percent(self):
        loyP = (1 - 2**(2*self.mlrry)) * 100
        return loyP
    
    def concat_data(self):
        loyP = self.loy_percent()
        concat_mlrr = pd.concat([self.mlrr, loyP], axis = 1)
        concat_mlrr.columns = ['id', 'sex', 'mlrry', 'mlrrx', 'loyP']
        return concat_mlrr
   
    def write_csv(self, output_file):
        output = self.concat_data()
        output.to_csv(output_file, index=False, sep='\t')
