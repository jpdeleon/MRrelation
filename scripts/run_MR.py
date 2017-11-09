#!/usr/bin/env python
'''
Created: 11/09
Input: c10_per_rad_stm.csv; run_MR.R
run_MR.R requires:
posterior_samples.savr; calc_mass_postpred.R

Output: KESPRINT-C10/*.ps & .txt

Purpose: estimtae mass of KESPRINT validated campaign 10
systems using MRrelation (Wolfgang 2017)

see also mass estimation of KESPRINT targets using M-R relation.ipynb

This script reads the list of validated planets (epic)
with their radius derived from transit observation.

The epics number, radius, and radius error is fed
as argument to the run_MR.R script which produces 
the .ps plot and posterior 
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
    !Rscript run_MR.R $epic $let $r $r_err
