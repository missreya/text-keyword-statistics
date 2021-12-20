## Project Information
- This script will take all text files along with a keyword file and generate a file with text statistics and keyword counts
- Refer to **ds-swe-tech-assessment-prompt.md** for all information and requirements

## Text File Requirements:
- All text file inputs must be .txt text files
- File text is in English with words 
- Text should be separated by whitespace (i.e. not comma separated values)
- Keyword file must be placed in the same directory as your text files
- Text files recommended to be UTF-8

## Script Info: 
- User must provide a file directory containing the text files they wish to process 
- This script uses two optional arguments: 
    - -t or --textpath: 
        - Full folder directory containing text files 
        - Default: current working directory
    - -k or --keywordfile: 
        - Keyword text file name
        - Default: keyword.txt in current working directory
    - This is called as the following:
    ``` 
    $ python text_keyword_statistics.py -t "c:/user/yourtextfiles" -k "yourkeywords.txt"
    ```

## Output Info:
- This script will print out the elasped time for processing all text files in the terminal
- A text file will be generated in the working directory of the script containing the text statistics titled "statistics.txt"
    - Option to change this to end with date and time in script comments

## Docker Container Info:
- Since this script produces a text file, docker must be ran with daemon in order to pull the file out of the container
- this can be performed by first running with daemon in background:
    ```
    $ docker-compose up -d
    ```
- copy the CONTAINER ID in the list of containers:
    ```
    $ docker container ls
    ```
- then pull the output "statistics.txt" file to your directory:
    ```
    $ docker cp [CONTAINER ID]:/usr/src/app/statistics.txt ./
    ```