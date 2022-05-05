"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from task_05.py:
>>> test_dir = Path("C:\", "Users", "MyNotebook", "PycharmProjects", "BigData_Podshivalova", "hw7")
>>> universal_file_counter(test_dir, "txt")
12
>>> universal_file_counter(test_dir, "txt", str.split)
12

"""
from pathlib import Path
from typing import Optional, Callable
import os

# if there is no tokenizer: read all the files in the specified directory,
# and then count the number of lines in each file


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    file_to_pars = []
    line_count = 0
    for file_name in os.listdir(dir_path):
        if file_name.strip().split('.')[1] == file_extension:
            file_to_pars += [file_name]
        for file_ in file_to_pars:
            with open(file_) as file:
                if tokenizer is None:
                    line_count += len(file.readlines())
                else:
                    line_count += len(tokenizer('\n'.join(file.readlines())))
    return line_count


if __name__ == '__main__':
    import doctest
