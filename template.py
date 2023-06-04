import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name='Usa_elections'

list_of_files = [
    ".github/workflows/.gitkeep",
    "airflow-dags/dags/common.py",
    "airflow-dags/dags/us_elections_pipeline.py",
    "sql",
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "params.yaml",
    "driver.py",
    "app.py",
    "main.py",
    "DockerFile",
    "requirements.txt",
    "setup.py",
    "research/experiment.ipynb"
]

for file_path in list_of_files:
    filepath= Path(file_path)
    #create folder if it doesn't exist
    filedir,file_name = os.path.split(filepath)
    if filedir!= "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created folder - {filedir} and file - {file_name}")
    
    if  (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"created empty file - {filepath}")
    else:
        logging.info(f"file already exists- {filepath}")

