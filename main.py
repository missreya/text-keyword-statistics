# Import Module
import os
import numpy as np
import re
import time
import argparse
from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class FileData:
    lines: List[str]
    tokens: List[str]
    keyword_counter: Dict[str, int]
    duplicate_counter: Dict[str, int]
    
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
        if file.startswith("statistics_") or file==(os.path.basename(keyword_file)):
            continue

        # Check if file is in text format
        elif file.endswith(".txt"):
            file_path = f"{path}\{file}"
            files_to_process.append(file_path)
            
    return files_to_process

# Text file processing and statistic function
def process_text_file(file, keyword_list, statistics: FileData):
    
    #Open file for processing in read-only and ignores encoding errors
    with open(file, mode="r", errors="ignore") as f: 
        for line in f:
            line = line.rstrip().lstrip()
            if len(line) < 1:
                continue

            #Update counters; dupe counter starts at -1 so the first instance is not counted as a dupe
            statistics.duplicate_counter[line] = statistics.duplicate_counter.get(line, -1) + 1
            statistics.lines.append(len(line))
            statistics.tokens.append(len(line.split(" ")))

            #Checks for keyword in line and adds count to dictionary
            for keyword in keyword_list:
                if re.search(r"\b" + str(keyword) + r"\b", line):  
                    statistics.keyword_counter[keyword] = statistics.keyword_counter.get(keyword, 0) + 1
    

def write_output(statistics: FileData):
    # Determine dupes (i.e. keys with value over 1 dupe counter)
    dup_num = sum(statistics.duplicate_counter.values())
    dupes = "num dupes\t" + str(dup_num)

    # Calculate line & token results from the stat counter
    line_stats = "med length\t" + str(np.median(statistics.lines)) +"\n" + "std length\t" + str(np.std(statistics.lines))
    token_stats = "med tokens\t" + str(np.median(statistics.tokens)) +"\n" + "std length\t" + str(np.std(statistics.tokens))
    line_token_stats = line_stats + "\n" + token_stats

    #Calculate keyword results from keyword counter
    keywords = str()
    for key, value in sorted(statistics.keyword_counter.items()):
        keywords = keywords + key + "\t" + str(value) + "\n"

    #Create result text file
    now = datetime.now()
    statistics_file_path = f"{os.getcwd()}\\statistics_{now.strftime('%Y%m%d-%H%M%S')}.txt"
    with open(statistics_file_path, 'w') as r:
        r.write(f"{dupes}\n{line_token_stats}\n{keywords}")

def main():
    
    parser = argparse.ArgumentParser(description='Generates character and keyword statistics from text files')
    parser.add_argument('-t', '--textpath', type = str, default=f"{os.getcwd()}", help='Folder directory with text files. (Default = working directory)')
    parser.add_argument('-k', '--keywordfile', type = str, default="keyword.txt", help='Keyword file in same folder as text files. (Default = keyword.txt)')
    args = parser.parse_args()
    args.keywordfile = f"{args.textpath}\{args.keywordfile}" 

    keyword_list = init_keyword(args.keywordfile)
    files_to_process = file_iterate(args.textpath, args.keywordfile)


    file_stats = FileData(lines=list(), tokens=list(), keyword_counter=dict.fromkeys(keyword_list, 0), duplicate_counter=dict())

    for file in files_to_process:
        process_text_file(file, keyword_list, file_stats)
    write_output(file_stats)

if __name__ == '__main__':
    main()