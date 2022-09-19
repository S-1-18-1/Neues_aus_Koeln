import csv
from fileinput import filename
import os
import re
import datetime
import pandas as pd


data_path ="data"
output = "output/overview.csv"
output_collected_lines = "output/collected_lines.txt"
statistics = {}

# basic counter for 
locales_not_found=0
locales_counter_all = 0
neues_not_found=0
neues_counter_all = 0

week_day_names = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

collected_lines = ""

for root, dir, files in os.walk(data_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        with open (file_path, 'r') as f:
            lines = []
            for line in f:
               lines.append(line)
        locales_counter = 0
        neues_counter = 0
        day = datetime.date(day=int(file_name.split("_")[2]), month=int(file_name.split("_")[1]), year=int(file_name.split("_")[0]))
        week_day = day.weekday()
        statistics[str(file_name)] = [day]
        for index, current_line in enumerate(lines):
            if re.match("\w*[TLk][oes][ce]a[lt]es($|\.)", current_line): 
                # collected_lines += current_line + "\n"
                locales_counter +=1
            elif re.match("aus [RKtA][öo][li](n|\.)", current_line) and re.match("[TNLn]eues", lines[index-1]):                
                neues_counter +=1
                collected_lines += lines[index-1]
                collected_lines += current_line + "\n"
            elif re.match("(aus [RKtA][öo][li]n)(\.)?$", current_line) and ("Anzeiger" in lines[index-1] or any(name in lines[index-1] for name in week_day_names) or "Seite" in lines[index-1] or len(lines[index-1])<=7) and len(lines[index-1])<70:
                
                neues_counter +=1
                collected_lines += lines[index-1]
                collected_lines += current_line + "\n"
            elif re.match("[Aa]us [RKtA][öo][li]n-", current_line):
                print(current_line)
                
               
        statistics[str(file_name)].append(locales_counter)
        statistics[str(file_name)].append(neues_counter)
        statistics[str(file_name)].append(week_day)
        if locales_counter ==0 and int(file_name.split("_")[0]) < 1908:
            locales_not_found += 1
        if neues_counter==0 and int(file_name.split("_")[0]) >= 1908:
            neues_not_found += 1
        locales_counter_all += locales_counter
        neues_counter_all += neues_counter


with open(output, "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Ausgabe", "Datum", "Locales?", "Neues aus Köln?", "Wochentag"])
    for ausgabe in statistics:
        writer.writerow([ausgabe, statistics[ausgabe][0], statistics[ausgabe][1], statistics[ausgabe][2], statistics[ausgabe][3]])


# to check which regex work best
print("Zeitungen, in denen Locales nicht gefunden wurde: %i" %locales_not_found)
print ("Insgesamte Anzahl an Locales: %i" %locales_counter_all)
print("Zeitungen, in denen Neues aus Köln nicht gefunden wurde: %i" %neues_not_found)
print("Insgesamte Anzahl an Neues aus Köln: %i" %neues_counter_all)

with open(output_collected_lines, "w") as file:
    file.write(collected_lines)

