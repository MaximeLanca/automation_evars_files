#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

PATH_ADMIN_FOLDER = 'C:\\AVEVA\\Administration\\2.1\\Administration\\'
RELATIF_PATH = '%CD%'
VARIABLE_TO_DETECTE = '%~dp0'
script_path = Path(__file__).resolve()
script_dir = script_path.parent


def __init__(self):
    pass

def search_customEvars():


#Fonction pour trouver le TRIgramme
def get_trigram():
    
    pattern = re.compile(r'^([A-Z]{3})')
    return pattern

def create_folders():
    trigram_project = get_trigram()
    name_folder = trigram_project + 'load'
    name_folder.mkdir(parents=True, exist_ok = True)

    os.chdir(script_dir +'/'+name_folder )

    
def read_admin_files():
    pass

if __name__ == "__main__":
    app = Main()
    app.run()


# mettre le script avec evarsTRI
#