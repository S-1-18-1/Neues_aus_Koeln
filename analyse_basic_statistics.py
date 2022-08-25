import pandas as pd


df = pd.read_csv("overview.csv", index_col=0, header=0)
df["Datum"] = pd.to_datetime(df['Datum'],format='%Y-%m-%d')
df = df.sort_values(by=['Datum'])

# drop duplicates because if there are two issues in one day, one is likely to be a Special issue
df_cleaned_locales = df.drop_duplicates(subset="Datum", keep=False)
df_cleaned_neues = df.drop_duplicates(subset="Datum", keep=False)


df_cleaned_locales = df_cleaned_locales.loc[(df['Locales?'] == 0) & (df['Datum']<='1907-12-31'),:]
df_cleaned_locales = df_cleaned_locales.sort_values(by=['Datum'])

df_cleaned_neues = df_cleaned_neues.loc[(df['Neues aus Köln?'] == 0) & (df['Datum']>'1907-12-31'),:]
df_cleaned_neues = df_cleaned_neues.sort_values(by=['Datum'])

print(df_cleaned_neues.to_string())
df_cleaned_neues.to_csv("cleaned_neues.csv")
#(df['Locales?'] == 0) & 

#print(df_cleaned_locales.to_string()) 
df_counts = df.groupby(pd.Grouper(key='Datum', axis=0, freq='Y')).size()


df = df.groupby(pd.Grouper(key='Datum', axis=0, freq='Y')).sum()
df = df.assign(Anzahl = df_counts)

# Wie oft "Lokales" pro Kategorie
df["Schnitt Lokales"] = df["Locales?"]/df["Anzahl"]
df["Schnitt Neues"] = df["Neues aus Köln?"]/df["Anzahl"]
#df = df.cumsum()
plot = df["Schnitt Neues"].plot()
plot = df["Schnitt Lokales"].plot()
plot.get_figure().savefig("out.png")
#print(df)