#!/home/emily/anaconda2/bin/python
###############################################################################
# Version: 1.1
# Last modified on: 3 April, 2016 
# Developers: Michael G. Epitropakis
#      email: m_(DOT)_epitropakis_(AT)_lancaster_(DOT)_ac_(DOT)_uk 
###############################################################################
from cec2013.cec2013 import *
import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt

def main():

	problem = int(sys.argv[1])

	# Create function
	f = CEC2013(problem)

	lx = f.get_lbound(0)
	ly = f.get_lbound(1)
	ux = f.get_ubound(0)
	uy = f.get_ubound(1)

	xs = np.linspace(lx, ux, 1000)
	ys = np.linspace(ly, uy, 1000)
	xs, ys = np.meshgrid(xs, ys)
	# print(lx, ly, ux, uy, xs, ys)	
	# zs = np.array([f.evaluate([x, y]) for x in xs for y in ys])
	zs = np.array([f.evaluate([x,y]) for x,y in zip(np.ravel(xs), np.ravel(ys))])
	# print(zs)
	zs = zs.reshape(xs.shape)
	# zs = zs.reshape(len(xs), len(ys))
	# print(zs)
	plt.imsave("fun_"+ str(problem) +".jpg", zs, format="jpg", cmap="gray")
	
	with open("fun_"+str(problem)+"_bounds.csv", "w") as outfile:
		outfile.write(" ".join(["x:", str(lx), str(ux)]) + "\n")
		outfile.write(" ".join(["y:", str(ly), str(uy)]) + "\n")
		outfile.write(" ".join(["z:", str(zs.min()), str(zs.max())]) + "\n")

	#print(df)
	# Evaluate :-)
	# x = np.ones(2)
	# value = f.evaluate(x)




if __name__ == "__main__":
	main()
