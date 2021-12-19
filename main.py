# Import Module
import os
import numpy as np
import re
import time

# Change directory to entered Folder Path
def init_directory(path=None):
    if path is None:
        path = input("Enter Folder Path Containing Text Files: ")
        if len(path) <1: 
            path = os.getcwd() 

    # Select keyword file. Leaving blank to auto enter default filename "keyword.txt". 
    keyword_file = input("Enter Keyword File: ")
    if len(keyword_file) <1: 
        keyword_file = "keyword.txt" 
    return path, keyword_file
    
# Initialization (keywords)
def init_keyword(keyword_file):
    keyword_list = list() 

    # Copy keywords from file into keyword set
    with open(keyword_file, "r") as k:
        for kw in k:
            keyword_list.append(kw.rstrip())
    return keyword_list

# Iterate through all files and creates list of files to process
def file_iterate(path, keyword_file):
    files_to_process = list()
    for file in os.listdir(path):
        
        # Skip the keyword and statistics files
        if file.startswith("statistics_") or file==(keyword_file):
            continue

        # Check if file is in text format
        elif file.endswith(".txt"):
            file_path = f"{path}\{file}"
            files_to_process.append(file_path)
            
    return files_to_process

# Text file processing and statistic function
def process_text_file(file, keyword_list):
    start_time_file = time.perf_counter()
    
    #Initialization (statistics)
    keyword_counter = dict.fromkeys(keyword_list, 0) #turns keyword list into dict keys with value 0 
    dupe_counter = dict() #tracks all lines to count dupes
    line_list = list()
    token_list = list() 

    #Open file for processing in read-only and ignores encoding errors
    with open(file, mode="r", errors="ignore") as f: 
        for line in f:
            line = line.rstrip().lstrip()
            if len(line) < 1:
                continue

            #Update counters; dupe counter starts at -1 so the first instance is not counted as a dupe
            dupe_counter[line] = dupe_counter.get(line, -1) + 1
            line_list.append(len(line))
            token_list.append(len(line.split(" ")))

            #Checks for keyword in line and adds count to dictionary
            for keyword in keyword_list:
                if re.search(r"\b" + str(keyword) + r"\b", line):  
                    keyword_counter[keyword] = keyword_counter.get(keyword, 0) + 1
    
    # Determine dupes (i.e. keys with value over 1 dupe counter)
    dup_num = sum(dupe_counter.values())
    dupes = "num dupes\t" + str(dup_num)

    # Calculate line & token results from the stat counter
    line_stats = "med length\t" + str(np.median(line_list)) +"\n" + "std length\t" + str(np.std(line_list))
    token_stats = "med tokens\t" + str(np.median(token_list)) +"\n" + "std length\t" + str(np.std(token_list))
    statistics = line_stats + "\n" + token_stats

    #Calculate keyword results from keyword counter
    keywords = str()
    for key, value in sorted(keyword_counter.items()):
        keywords = keywords + key + "\t" + str(value) + "\n"

    #Create result text file
    statistics_file_path = f"{os.path.dirname(file)}\\statistics_{os.path.basename(file)}"
    with open(statistics_file_path, 'w') as r:
        r.write(f"{dupes}\n{statistics}\n{keywords}")
    stop_time_file = time.perf_counter()
    print(f"Completed file: {file} in {stop_time_file - start_time_file:0.4f} seconds") 

def main():
    path, keyword_file = init_directory()
    keyword_list = init_keyword(keyword_file)
    files_to_process = file_iterate(path, keyword_file)

    for file in files_to_process:
        process_text_file(file, keyword_list)

if __name__ == '__main__':
    main()