## Project Information
- This script will take all text files along with a keyword file and generate a file with text statistics and keyword counts
- Refer to **ds-swe-tech-assessment-prompt.md** for all information

## Script Overview
- User must input a file directory which should contain the all of the files of text to process (defaults to current working directory)
- User then must provide keyword file name in the same directory (defaults to keyword.txt)
- The output file will be placed in the same directory titled as "statistics_" with the date and time

### File Requirements:
- All file inputs are .txt text files
- File text is in English with words separated by spaces (i.e. not comma separated)
- Keyword file must be in the same directory as the text files
- This script uses two optional args: 
    -t or --textpath: complete file path to folder with text files 
        Default: current working directory (type: string)
    -k or --keywordfile: file name of keyword text file
        Default: keyword.txt in current working directory (type: string)