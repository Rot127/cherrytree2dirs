import os
from pathlib import Path

pwd = os.getcwd() + "/"

for subdir, dirs, files in os.walk(pwd):
    for f in files:
        if f[-2:] == "py": 
            continue
        sub_dir_names = f.split("--")[:-1]
        if len(sub_dir_names) == 0:
            continue
        new_sub_dir = "/".join(sub_dir_names) + "/"
        Path(new_sub_dir).mkdir(parents=True, exist_ok=True)
        with open(pwd + f, "r") as f_cherry: 
            with open(new_sub_dir + "/" + f.split("--")[-1], "w+") as f_tu:
                f_tu.writelines(f_cherry.readlines())

