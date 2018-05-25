# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 01:33:28 2016

@author: Surath
"""

import numpy as np
import skfuzz as fuzz

def main():
    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    health = fuzz.Antecedent(np.arange(0, 101, 1), 'health')
    score = fuzz.Antecedent(np.arange(0, 101, 1), 'score')
    class_packs = fuzz.Antecedent(np.arange(0, 11, 1), 'class packs')
    out_of_bounds = fuzz.Antecedent(np.arange(0, 2, 1), 'out of bounds')
    result_rate = fuzz.Consequent(np.arange(0, 101, 1), 'result rate')
    
    # Auto-membership function population is possible with .automf(3, 5, or 7)
    health.automf(3)
    score.automf(3)
    class_packs.automf(3)
    out_of_bounds.automf(3)
    
    # Custom membership functions can be built interactively with a familiar,
    # Pythonic API
    result_rate['low'] = fuzz.trimf(result_rate.universe, [0, 0, 40])
    result_rate['medium'] = fuzz.trimf(result_rate.universe, [0, 40, 70])
    result_rate['high'] = fuzz.trimf(result_rate.universe, [40, 70, 100])
    
    health.view()