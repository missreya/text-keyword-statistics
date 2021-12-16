# Sondermind Data Science SWE Technical Assignment

The following task is meant to get a sense of your technical skillset.
Use any documentation or resources you need to complete the task.
Please complete the task and submit your code via the link you were
given when you received these instructions. When submitting your code,
please do so either using a link to a publicly viewable repository
(e.g. github/gitlab/etc) or upload a tarball containing your repository.

Please use either Python or Golang to complete this assignment.

## Task

In our work, we often deal with large amounts of streaming text data.
It is imperative that we be able to process that data as quickly and as efficiently as possible.

Write a program that reads lines of text from one or more files and computes statistics on the lines consumed.
An additional file containing keywords, with one keyword per line, will also be specified at runtime.
The statistics file will be a tab-separated text file with the following output:

```
num dupes   d
med length  lm
std length  ls
med tokens  tm
std length  ts
keyword_a   ka
...
keyword_n   kn
```

where `d` represents the number of exactly duplicated lines seen, `lm` is the median length of lines
(number of unicode characters), `ls` is the standard deviation of line length, `tm` is the median
number of tokens (via whitespace tokenization) per line, `ts` is the standard deviation of tokens
per line, and `ka` ... `kn` represent the total number of lines the keyword was seen on, sorted
alphabetically.

The program should process lines concurrently. Attention should be paid to required memory footprint
and runtime complexity. In some cases, approximate results may be acceptable.

## Results

Your repository should contain the following items:

1. All code used to complete the assignment
2. A docker-compose file that allows us to replicate your work by running `docker-compose up`
3. Benchmarks for hot-path components of the program