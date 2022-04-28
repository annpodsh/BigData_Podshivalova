"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator


# read the data from the file in int format and write it to the sheet

def merge_sorted_files(file_list: List[Union[Path, str], ...]) -> Iterator:
    numb_list = []
    for file_name in file_list:
        with open(file_name) as file:
            numb_list += [int(x) for x in file.read().strip().split()]

# sort the sheet and iterate it at the output
    
    numb_list.sort()
    return iter(numb_list)
