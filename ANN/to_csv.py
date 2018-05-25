import pandas as pd 
import csv
import random


def convert(data_set, column):
    print("inside convert")
    df = pd.DataFrame(data_set, columns = column)
    df.to_csv('F:\\Projects\\FYP\\ANN\\player_profile.csv', index=False)

        '''data_set = {'health': health, 'score': score, 'class_packs': class_packs,
         'out_of_bounds': out_of_bounds, 'result_rate': result_rate}'''

        


                
                