import os
from pathlib import Path # take care of the path

print(Path("a\b\c.txt"))

list_of_files=[
    ".github/workflows",
    ".src/__init__.py",
    ".src/components/__init__.py", # pipeline, collection of different components
    ".src/components/data_ingestion.py",
    ".src/components/data_transformation.py",
    ".src/components/model_training.py",
    ".src/components/model_evaluation.py"
    
]