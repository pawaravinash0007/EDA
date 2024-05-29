import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Wine Data Analysis")
st.sidebar.title("Wine Data Analysis")

def load_data():
	wine_data=pd.read_csv("winequality.csv")
	return wine_data
df=load_data()
pr = ProfileReport(df, explorative=True)
if  st.sidebar.checkbox("Visulization",False): 
	#if  st.sidebar.checkbox("Visulization",False):
	graph=st.sidebar.selectbox("Select Graph",("CountPlot","Heatmap","ScatterPlot","ScatterPlot1","ScatterPlot2","3D","Hist","BoxPlot"))
	if graph=="CountPlot":
		fig,ax=plt.subplots()
		ax=sns.countplot(data=df,x="quality",color="blue")
		plt.tight_layout(rect=(0,0,1,1))
		plt.title("Wine Quality Distribution")
		st.pyplot(fig)
	if graph=="Heatmap":
		fig, ax = plt.subplots(1, 1, figsize=(25,15)) # row =1 col=1 size = 14,8
		ax=sns.heatmap(df.corr(),
	            ax=ax,
	            cmap="bwr",  #cmap: The mapping from data values to color space.
	            annot=True,  #annot: If True, write the data value in each cell.
	            fmt='.2f',   #fmt: String formatting code to use when adding annotations.
	            linewidths=.5, #linewidths: Width of the lines that will divide each cell.
	            annot_kws={"size": 20})
		plt.title("Wine attributes and their Correlation",fontsize=20,fontweight="bold")
		plt.tight_layout(rect=(0,0,1,1))
		plt.show()
		st.pyplot(fig)
	if graph=="ScatterPlot":
		fig, ax = plt.subplots()
		ax=sns.scatterplot(data=df,y="free sulfur dioxide",x="total sulfur dioxide",hue="quality",palette="deep")
		plt.tight_layout()
		st.pyplot(fig)
	if graph=="ScatterPlot1":
		fig, ax = plt.subplots()
		ax=sns.scatterplot(data=df,y="fixed acidity",x="total sulfur dioxide",hue="quality",palette="deep",legend="full")
		plt.tight_layout()
		st.pyplot(fig)
	if graph=="ScatterPlot2":
		fig, ax = plt.subplots()
		ax=sns.scatterplot(data=df,y="fixed acidity",x="pH",hue="quality",palette="deep",legend="full")
		plt.tight_layout()
		st.pyplot(fig)
	if graph=="3D":
		fig = plt.figure(figsize=(16, 12))
		ax = fig.add_subplot(111, projection='3d') # rows=1 col=1 index= 1
		x = df['residual sugar']
		y = df['free sulfur dioxide']
		z = df['total sulfur dioxide']
		ax.scatter(x, y, z, s=50, alpha=0.6, edgecolors='w')
		ax.set_xlabel('Residual Sugar')
		ax.set_ylabel('free sulfur dioxide')
		ax.set_zlabel('Total sulfur dioxide')
		plt.show()
		plt.tight_layout()
		st.pyplot(fig)
	if graph=="Hist":
		fig, ax = plt.subplots()
		ax=sns.histplot(df["quality"],kde=True)
		plt.tight_layout()
		st.pyplot(fig)
	if graph=="BoxPlot":
		fig, ax = plt.subplots()
		ax=sns.boxplot(x='quality', y='alcohol', data = df, showfliers=False)
		plt.tight_layout()
		st.pyplot(fig)
else:
	st.subheader("1. To Display Graph Select Visulization")
	st.subheader("2. To display Raw Data Select Raw Data")
	st.subheader("3. To Display Pandas Profile Report Select Profile Report")
	
		


if  st.sidebar.checkbox("Raw Data",False):
	st.write(df)

if  st.sidebar.checkbox("Profile Report",False):
	st_profile_report(pr)
	
