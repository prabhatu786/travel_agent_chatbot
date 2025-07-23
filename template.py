
import os
from pathlib import Path

package_name="agent"

list_of_files=[
    "github/workflows/.gitkeep",
    f"{package_name}/__init__.py",
    f"{package_name}/Data_loader.py",
    f"{package_name}/Model_loader.py",
    f"{package_name}/Flow_chain.py",
    f"{package_name}/main.py",
    f"{package_name}/logger.py",
    f"{package_name}/exception.py",
    "requirements.txt",
    ".env",
    "setup.py",
]


# here will create a directory

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")

# here will use the file handling
