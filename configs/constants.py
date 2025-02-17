import os
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

LOG_DIR = os.path.join(ROOT_DIR, "log")
RESULTS_DIR = os.path.join(ROOT_DIR, "results")
CONFIGS_DIR = os.path.join(ROOT_DIR, "configs")
DATA_DIR = os.path.join(ROOT_DIR, "data")

FAILED_PATH = os.path.join(RESULTS_DIR, 'failed.txt')
SUCCESS_PATH = os.path.join(RESULTS_DIR, 'success.txt')
DATABASE_PATH = os.path.join(DATA_DIR, 'data.db')
REFS_PATH = os.path.join(CONFIGS_DIR, "REFS.txt")
LOG_PATH = os.path.join(LOG_DIR, 'log.log')
FARM_PATH = os.path.join(CONFIGS_DIR, "farm.txt")
REGISTER_PATH = os.path.join(CONFIGS_DIR, "register.txt")
PROXIES_PATH = os.path.join(CONFIGS_DIR, "proxies.txt")