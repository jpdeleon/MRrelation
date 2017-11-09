#!/usr/bin/env Rscript

#setwd("~/github/MRrelation/")
scripts="~/github/MRrelation/scripts/"
data="~/github/MRrelation/data/"
outputdir="~/github/MRrelation/KESPRINT-C10/"

args <- commandArgs(trailingOnly = TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)==0) {
  stop("(1)epic (2)planet_letter (3)planet_radius (4)planet_radius_err", call.=FALSE)
} else if (length(args)==1) {
  stop("(1)epic (2)planet_letter (3)planet_radius (4)planet_radius_err", call.=FALSE)
}

#parse arguments
epic    = args[1]
planletter = args[2]
planrad = as.double(args[3])
planraderr = as.double(args[4])

print(paste('------',epic,'------'))

#Generate samples from your planet radius distribution
numsamples = 100000 


#Read the posterior samples into R
load(paste(data,"posterior_samples.savr",sep=""))

#Read in the code that computes the mass posterior predictive distribution
source(paste(scripts,"calc_mass_postpred.R",sep=""))

print("---calculating posterior mass distribution---")

#Calculate the posterior predictive mass distribution
postpred = massguess_individpl(postsamp_eqn2_baseline,numsamples,planrad,raderr=planraderr)

masses = postpred$masses

print("Prediction: SUCESS")

#A plot showing the joint mass-radius distribution for this individual planet
#save plot as a png file
fname1 <- paste(epic,planletter,".png",sep="")
plotname = paste(outputdir,fname1,sep="")
png(file=plotname)
#postscript(file=plotfile,width=10,height=8)
plot_individMR(postpred$radii,postpred$masses)
#dev.copy(png, plotname)
dev.off()

fname2 <- paste("massrad_postpred_",epic,planletter,".txt",sep="")
#Write samples from joint mass-radius distribution into text file
write.table(postpred,file=paste(outputdir,fname2,sep=""))
