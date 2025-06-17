# CODDED BY RAYZER
import os  # By Rayzer
import sys  # By Rayzer

try:  # By Rayzer
    import requests  # By Rayzer
    import rich  # By Rayzer
except ImportError:  # By Rayzer
    os.system(f"{sys.executable} -m pip install requests rich")  # By Rayzer

os.system(f"{sys.executable} main.py")  # By Rayzer
