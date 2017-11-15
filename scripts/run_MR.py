#!/usr/bin/env python
'''
Created: 11/09
Updated: 11/14

Input: c10_per_rad_stm_kp.csv; run_MR.R
run_MR.R requires:
posterior_samples.savr; calc_mass_postpred.R

Output: KESPRINT-C10/*.png & .txt

Purpose: estimate mass of KESPRINT validated campaign 10
systems using MRrelation (Wolfgang 2015)

see also mass estimation of KESPRINT targets using M-R relation.ipynb

This script reads the list of validated planets (epic)
with their radius derived from transit observation.

The epic number, planet letter, radius, and radius error 
are fed as arguments to the run_MR.R script which produces 
the plots (.png) and posterior samples of mass prediction (.txt) 
The R script follows the example in github.
'''

import pandas as pd

#stellar parameters
df = pd.read_csv('c10_per_rad_stm.csv')

epics      = df['epic']
letter     = df['pl']
radii      = df['r']
radii_errs = df['r_err']

n=-1 #run all
for epic,let,r,r_err in zip(epics[:n],letter[:n],radii[:n],radii_errs[:n]):
    #print(epic)
    ###verbose
    !Rscript run_MR.R $epic $let $r $r_err
    ###use below to hide output in terminal
    !Rscript run_MR.R $epic $let $r $r_err 2&>1 >/dev/null
