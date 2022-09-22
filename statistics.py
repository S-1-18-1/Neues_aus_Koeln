import pandas as pd 
import os
from lxml import etree as ET
import matplotlib.pyplot as plt

def print_statistics(path, output):
    """takes a collection of xml files and outputs basic statistics

    :param path: path to the xml files
    :type path: str
    :param output: path to the output figure
    :type output: str
    """

    parser = ET.XMLParser(remove_blank_text=True)

    # list for later df rows
    rows = []
    
    # filling in the list 
    for root, dir, files in os.walk(path):
        for file_name in files:
            full_path = os.path.join(path, file_name)
            tree = ET.parse(full_path, parser)
            id = tree.find(".//ID").text
            year = tree.find(".//year").text
            #count = len(tree.findall(".//story"))
            count = int(tree.xpath("count(//text[text()])"))
            rows.append({"ID": id, "Jahr": year, "Geschichten": count})

    # building the initial dataframe
    df_cols = ["ID", "Jahr", "Geschichten"]
    df = pd.DataFrame(rows, columns = df_cols)
    df = df.set_index('ID')
    df = df.sort_values(by=['Jahr'])

    # adding average value columns
    df_counts = df.groupby(pd.Grouper(key='Jahr', axis=0)).size()
    df_grouped = df.groupby(pd.Grouper(key='Jahr', axis=0)).sum()
    df_grouped = df_grouped.assign(Ausgaben = df_counts)
    df_grouped["Geschichten pro Ausgabe"] = df_grouped["Geschichten"]/df_grouped["Ausgaben"]

    #plotting
    plot = df_grouped.plot(y='Geschichten pro Ausgabe',color='green')
    plot.get_figure().savefig(output)
    print("Gesamtanzahl Geschichten: %s"%df_grouped["Geschichten"].sum())

if __name__ == '__main__':
    print_statistics("corpus","output/Schnitt.png")