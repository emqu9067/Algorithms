import matplotlib.pyplot as plt
import numpy as np
import math

class my2DPlot:
    def __init__(self,f,a,b):
            x = np.arange(a,b,0.01)
            y = f(x)
            self.p = plt.plot(x,y)
    def show(self):
            #this function shows the plot on your screen
            plt.show()
    def dotted(self):
            #this function changes the last plot to be dotted instead of solid
            self.p[-1].set_linestyle('dotted')
    def labels(self,x,y):
            #this plot changes the labels on the plot figure
            plt.xlabel(x)
            plt.ylabel(y)
    def addPlot(self,f):
            #this function adds multiple plots on a single figure
            x=self.p[0].get_data()[0]
            plt.plot(x,f(x))
    def color(self,colorName):
            #this function changes the color of the last plotted line
            self.p[-1].set_color(colorName)
    def logy(self):
            plt.yscale('log')
    def logx(self):
            plt.xscale('log')
    def save(self,fileName):
            plt.savefig(fileName)
