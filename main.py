# Import Module
import os
import numpy as np
import re
import time

# Change directory to entered Folder Path
path = input("Enter Folder Path Containing Text Files: ")
if len(path) <1: path = "C:/Users/Rena/Documents/My Stuff/Software/repos/text-statistics-keyword-search" #Default
os.chdir(path)

# Select keyword file. Leaving blank to auto enter default filename "keyword.txt". 
keyword_file = input("Enter Keyword File: ")
if len(keyword_file) <1: keyword_file = "keyword.txt" 

# Initialization (keywords)
kw_list = [] 
Start_keyword = time.perf_counter()

# Copy keywords from file into keyword list
with open(keyword_file, "r") as k:
    for kw in k:
        kw_list.append(kw.rstrip())
    k.close()
    Stop_keyword = time.perf_counter()
    print(f"Completed keyword list: {kw_list} in {Stop_keyword - Start_keyword:0.4f} seconds") 

# Text file processing and statistic function
def process_text_file(file_path):
    tic = time.perf_counter()

    #Initialization (statistics)
    stat_counter = {} #linenumber:(line_length, token_count)
    kw_counter = dict.fromkeys(kw_list, 0) #turns keyword list into dict keys with value 0 
    dupe_counter = {} #tracks all lines to count dupes

    #Open file for processing
    with open(file_path, "r") as f: 
        for i, line in enumerate(f):
            ##### Strips the line of all white space and punctuation before processing
            # line = re.sub(r'[^\w\s]', '', line.lstrip().rstrip()).lower()
            line = line.rstrip().lstrip()
            if len(line) < 1:
                continue

            #Update dupe counter
            dupe_counter[line] = dupe_counter.get(line, 0) + 1

            #Update stat counter with line and token statistics
            line_length = len(line)
            token_count = len(line.split(" "))
            stat_counter[i] = (line_length, token_count)

            #Checks for keyword in line and adds count to dictionary
            for keyword in kw_list:
                if re.search(r"\b" + str(keyword) + r"\b", line):  
                    kw_counter[keyword] = kw_counter.get(keyword, 0) + 1
        f.close()
    
    # Determine dupes (i.e. keys with value over 1 dupe counter)
    dup_num = 0
    for k, v in dupe_counter.items():
        if v> 1:
            # dup_num += 1 #number of unique lines that were duplicated
            dup_num = dup_num + v - 1 # total number of all duplicated lines
    dupes = "num dupes\t" + str(dup_num)

    # Calculate line & token results from the stat counter
    token_list = []
    line_list = []
    for key, value in stat_counter.items():
        line_list.append(value[0])
        token_list.append(value[1])
    stats_line = "med length\t" + str(np.median(line_list)) +"\n" + "std length\t" + str(np.std(line_list))
    token_list = "med tokens\t" + str(np.median(token_list)) +"\n" + "std length\t" + str(np.std(token_list))
    statistics = stats_line + "\n" + token_list

    #Calculate keyword results from keyword counter
    keywords = ""
    for key, value in sorted(kw_counter.items()):
        keywords = keywords + key + "\t" + str(value) + "\n"

    #Create result text file
    with open(statistics_file_path, 'w') as r:
        r.write(f"{dupes}\n{statistics}\n{keywords}")
        r.close()
    toc = time.perf_counter()
    print(f"Completed file: {file} in {toc - tic:0.4f} seconds") 
        
# Iterate through all files
for file in os.listdir():
    
    # Skip the keyword and statistics files
    if file.startswith("statistics_") or file==(keyword_file):
        continue

    # Check if file is in text format then goes to process function
    elif file.endswith(".txt"):
        file_path = f"{path}\{file}"
        statistics_file_path = f"{path}/statistics_{file}"
        process_text_file(file_path)
