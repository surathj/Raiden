# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:41:24 2016

@author: Surath
"""
import sys
import json
import numpy as np
import csv
import pandas as pd

def main():
    #get our data as an array from read_in()
    print("inside AI")
    lines = sys.stdin.readlines()
    lines_n = json.loads(lines[0])
    lines_id = lines_n[0]
    lines_data = lines_n[1]
    #lines_id = np.array(lines_n[0])
    #lines_data = np.array(lines_n[1])
    #print(type(np_lines_data[0][0]))
    #print(np_lines_data[0][0])
    print(lines_data)

    data_set = {'player_id': lines_id,'health': lines_data[0], 'score': lines_data[1], 'class_packs': lines_data[2],
         'out_of_bounds': lines_data[3], 'result_rate': 0}
    
    df = pd.DataFrame(data_set, columns = ['player_id', 'health', 'score', 'class_packs', 'out_of_bounds', 'result_rate'])
    df.to_csv('F:\\Projects\\FYP\\ANN\\player_data.csv', index=False)
    
    from_dataset = pd.read_csv('F:\\Projects\\FYP\\ANN\\player_data.csv', parse_dates=True)
    nf = pd.DataFrame(from_dataset, columns = ['result_rate'])
    result_data = []
    #print(nf)

    '''for i in range(0, len(nf)):
    	record = list(nf.iloc[i])
    	result_data.append(record)
    	print(result_data)'''
    
    print(lines_data)


#start process
if __name__ == '__main__':
    main()

