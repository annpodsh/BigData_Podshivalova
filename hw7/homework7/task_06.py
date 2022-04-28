"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Optional, Callable
import os

# if there is no tokenizer: read all the files in the specified directory,
# and then count the number of lines in each file


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    if tokenizer is None:
        file_to_pars = []
        line_count = 0
        for file_name in os.listdir(dir_path):
            if file_name.strip().split('.')[1] == file_extension:
                file_to_pars += [file_name]
        for file_ in file_to_pars:
            with open(file_) as file:
                line_count += len(file.readlines())
        print(line_count)
    if tokenizer is not None:
        pass
