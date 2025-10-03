#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

PATH_ADMIN_FOLDER = 'C:\\AVEVA\\Administration\\2.1\\Administration\\'
RELATIF_PATH = '%CD%'
VARIABLE_TO_DETECTE = '%~dp0'

#donne l'emplacement exact du script
script_path = Path(__file__).resolve()
#dossier contenant le script
script_dir = script_path.parent

def main():
    folders_project_list = check_projet_folders()
    get_trigram(folders_project_list )

def __init__(self):
    pass

def search_customEvars():
    pass

def check_projet_folders() -> list:
    folders_name = ['000','ISO','MAC','PIC','DFLTS','DIA','STE','TPL']
    missing_folders = []
    pattern = re.compile(r'^([a-z]{3}).*000$')
    folders_project_list = [name for name in os.listdir(script_dir) if re.search(pattern,name)]

    if folders_project_list is None:
        print('*' * 80)
        print("The folders necessary for the project to function aren't available.")
        print('*' * 80)
        exit()
    
    for name in folders_project_list:
        if name[3:] not in folders_name:
            missing_folders.append(name)
    if missing_folders is not None:
        print('*' * 80)
        print(f'Missing folders : {missing_folders}')
        print('*' * 80)
    return folders_project_list

def get_trigram(folders_project_list):
    
    first_trigram = folders_project_list[0][:3]

    if all(item.startswith(first_trigram) for item in folders_project_list):
        print('*' * 80)
        print(f"Found trigram project: {first_trigram}")
        print('*' * 80)
        return first_trigram
    else:
        print("Folders haven't the same trigram")
        exit()

def create_folders():
    pass
    """ trigram_project = get_trigram()
    name_folder = trigram_project + 'load'
    name_folder.mkdir(parents=True, exist_ok = True)

    os.chdir(script_dir +'/'+name_folder )
 """
    
def read_admin_files():
    pass

if __name__ == "__main__":
    main()


# mettre le script avec evarsTRI
#