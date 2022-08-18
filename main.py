import matplotlib.pyplot as plt
import pandas as pd

# base de dados
db_reg = pd.read_excel("C:\\Users\\inf077\\Documents\\regeneracao - médias.xlsx", engine="openpyxl")
db_fra = pd.read_excel("C:\\Users\\inf077\\Documents\\fragmento - médias.xlsx", engine="openpyxl")

T1_r = []
T2_r = []
T3_r = []

T1_f = []
T2_f = []
T3_f = []

m_regeneracao = ['T1_r', 'T2_r', 'T3_r']

m_fragmento = ['T1_f', 'T2_f', 'T3_f']

# formatação para a leitura do boxplot
for i, j in enumerate(db_reg.iloc[0, :]):
    T1_r.append(j)
for m, n in enumerate(db_reg.iloc[1, :]):
    T2_r.append(n)
for a, b in enumerate(db_reg.iloc[2, :]):
    T3_r.append(b)

db_trans = [T1_r, T2_r, T3_r]

fig, (ax1) = plt.subplots()

# rectangular box plot
bplot1 = ax1.boxplot(db_trans,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=m_regeneracao)  # will be used to label x-ticks
ax1.set_title('Rectangular box plot')

# adding horizontal grid lines
for ax in [ax1]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Three separate samples')
    ax.set_ylabel('Observed values')

plt.show()