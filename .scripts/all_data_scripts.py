import glob
import importlib.util
import os
import sys
from pathlib import Path

os.chdir(Path(__file__).parent.joinpath("data"))
sys.path.append(str(Path(__file__).parent.joinpath("data")))
for module in glob.glob("*.py"):
    path = Path(os.getcwd()).joinpath(module)
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
