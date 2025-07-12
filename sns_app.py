import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt      # ← fix 1
import warnings
warnings.filterwarnings('ignore')

sns.set_theme(style="whitegrid")
tips = sns.load_dataset("tips")

st.title("Seaborn app: tip data visualization")
st.write("This is a simple app to visualize the tips dataset using Seaborn.")

def display_plot(title, plot_fun):
    st.subheader(title)
    fig, ax = plt.subplots(figsize=(7, 5))   # ← fix 2
    plot_fun(ax=ax)
    st.pyplot(fig)
    plt.close(fig)
#to plot 
def scatter_plot(ax):
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", size="size", palette="deep",ax=ax)
    ax.set_title("Scatterplot of total bills vs tips")
def line_plot(ax):
    sns.lineplot(data=tips, x='size', y='total_bill', hue='sex',ci=None, markers='o',ax=ax)
    ax.set_title("lineplot of total bill vs sixe")
def bar_plot(ax): 
    sns.barplot(data=tips, x='day',y='total_bill', hue='sex', palette='muted',ax=ax)
    ax.set_title("barplot of total bill by day")
def box_plot(ax):
    sns.boxplot(data=tips, x='day', y='tip', hue='smoker', palette='pastel',ax=ax)
    ax.set_title("Boxplot of tips by day and smoker status")
def violen_plot(ax):
    sns.violinplot(data=tips, x='day', y='total_bill', hue='time', split=True, palette='dark',ax=ax)
    ax.set_title("violin plot of total bill by day and time")
def count_plot(ax):
    sns.countplot(data=tips, x='day', hue='smoker', palette='colorblind', ax=ax)
    ax.set_title("count plot of days by smoker status")
def reg_plot(ax):
    sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'s':50}, line_kws={'color':'black'},ax=ax)
    ax.set_title("regression plot of total bill vs tip")
def hist_plot(ax):
    sns.histplot(data=tips, x='total_bill', bins=20, kde=True, color='pink' ,ax=ax)
    ax.set_title("histogram of total bill with kde")
def strip_plot(ax):
    sns.stripplot(data=tips, x='day' , y='tip' , hue='sex', jitter=True, palette='Set1',ax=ax)
    ax.set_title("strip plot: tips by day and gender")
def kde_plot(ax):
    sns.kdeplot(data=tips, x='total_bill',hue='sex', fill=True, palette="tab10",ax=ax)
    ax.set_title("kde plot: total bill density by gender")

st.subheader("Select a plot type")
display_plot("Scatter plot", scatter_plot)
display_plot("Line plot", line_plot)
display_plot("Bar plot", bar_plot)
display_plot("Bax plot", box_plot)
display_plot("violen plot", violen_plot)
display_plot("Count plot", count_plot)
display_plot("Regression plot", reg_plot)
display_plot("histogram plot", hist_plot)
display_plot("Strip plot", strip_plot)
display_plot("KDE plot", kde_plot)