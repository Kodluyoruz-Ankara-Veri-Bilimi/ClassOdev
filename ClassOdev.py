# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:40:37 2020

@author: Asiye
"""
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns


class Information:
        
    def __init__(self,filename):
        self.file = pd.read_csv(open(filename,'rb'))
        
    def shape(self):
        print("------------SHAPE----------------")
        print(self.file.shape)
        print()
        
    def info(self):
        print("------------INFO----------------")
        print(self.file.info())
        print()
        
    def columns(self):
        print("------------COLUMNS----------------")
        print(self.file.columns)
        print()
    
    def describe(self):
        print("------------DESCRIBE----------------")
        print(self.file.describe())
        print()
    
    def head(self):
        print("------------HEAD----------------")
        print(self.file.head())
        print()
        
    def tail(self):
        print("------------TAIL----------------")
        print(self.file.tail())
        print()
        
    def corr_table(self):
        corr = self.file.corr()
              
        sns.heatmap(corr, 
        xticklabels=corr.columns,
        yticklabels=corr.columns,annot =True)
        plt.show()
              
        
        
class Visualizer:
    
    def __init__(self,data):
        self.data = data
           
    
    def boxplot(self,column):
        self.column = column
        
        sns.boxplot(x = self.column, data = self.data)
    
    def factorplot(self,column1,column2,hue):
        self.column1 = column1
        self.column2 = colomn2
        self.hue = hue
        
        sns.factorplot(self.column1, self.column2, hue = self.hue, data = self.data)
        
    
    def barplot(self,x,y,hue):
        
        self.x = x
        self.y = y
        self.hue = hue
        
        sns.barplot(x=self.x, y=self.y, hue = self.hue , palette="rocket", data = self.data)
        
        
    def scatter_plot(self, x,y):
        
        self.x = x
        self.y =y
        
        plt.scatter(x = self.x, y=self.y, data=self.data)
        plt.xlabel(self.x)
        plt.ylabel(self.y)

        
        
    def scatterplotmatrix(self, hue):
        
        self.hue = hue
        
        sns.pairplot(self.data, hue=self.hue)
        
    # Just numeric fields   
    def lineplot(self):
        sns.lineplot(data=self.data, palette="tab10", linewidth=2.5)
        
    def value_counts(self, column):
        self.column = column
        
        sns.countplot(self.column ,data = self.data)
        
        
    def relplot(self,x,y,hue):
        self.x =x
        self.y = y
        self.hue = hue
        
        sns.relplot(x=self.x, y=self.x, hue=self.hue, 
            sizes=(40, 400), alpha=.5, 
            height=6, data=self.data)
        
    def corr_headmap(self):
        corr = self.data.corr()
        
        f, ax = plt.subplots(figsize=(9, 6))
        sns.heatmap(corr, annot=True, fmt="d", linewidths=.5, ax=ax)


           

        
        
     
        
        

