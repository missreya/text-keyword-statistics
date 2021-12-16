### File Requirements for Github:
1. All code used to complete the assignment
2. A docker-compose file that allows us to replicate your work by running `docker-compose up`
3. Benchmarks for hot-path components of the program

### Requirements for Program Success:
- Intake multiple text files of "textblock" and one "keyword" text file
- Output is returned with all statistics as specified in the prompt in a new file
- Tokens are separated via whitespace tokenization (see Assumptions for details)
- Required memory footprint and runtime complexity is significant - include timer or resource usage on runs
- All keywords in file must appear in the output file. If keyword was not found, its value is 0. 

### Assumptions:
- File inputs are .txt 
- File text is in English with words in common syntax and separated by spaces (i.e. not comma separated)
- Keywords do not contain any special characters (while may still work, it may process oddly)
- Keyword search does not need to be case sensitive
- Tokens are split by whitespace only (whitespace tokenization) and therefore may contain punctuation
- Lines are split by specifically new line "\n" whitespace. 
- "num dupes" are **total number of duplicated lines** (not number of unique lines that were duplicated)
- keyword count increases by one if keyword is in a line regardless of total keyword appearances in that line

## Statistic Counters:
num dupes   d ----- represents the number of exactly duplicated lines seen
med length  lm ---- median length of lines (number of unicode characters)
std length  ls ---- standard deviation of line length
med tokens  tm ---- median number of tokens (via whitespace tokenization) per line
std length  ts ---- standard deviation of tokens per line

## Keyword Counts:
keyword_a   ka ---- total number of lines the keyword was seen on, **sorted alphabetically**.
...
keyword_n   kn

## Remaining work:
- Update code to address answers to questions (if received)
- Add benchmarks to hot paths
    - May include removing the current timers
- Create official testing suite
- Investigate if hot path items have room for more optimization
    - blocks?
- Add in parameters for approximation for heavy-data lines if timer surpasses a certain time?
- Create the Docker file and test
- Once complete:
    - Remove the default file path