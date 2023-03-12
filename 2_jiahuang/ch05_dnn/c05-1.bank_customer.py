# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2023.3.12
# Bank Customer


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    df_bank = pd.read_csv("./data/BankCustomer.csv")
    print(df_bank.head())

    # 显示数据分布情况
    features = ['City', 'Gender', 'Age', 'Tenure', 'ProductsNo', 'HasCard', 'ActiveMember', 'Exited']
    fig = plt.subplots(figsize=(15, 15))
    for i, j in enumerate(features):
        plt.subplot(4, 2, i+1)
        plt.subplots_adjust(hspace=1.0)
        sns.countplot(x=j, data=df_bank)
        plt.title("No. of costumers")
    plt.show()      # pycharm中要加才会显示图像

