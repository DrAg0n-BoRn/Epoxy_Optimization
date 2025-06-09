from pathlib import Path
import os
import sys

# Set the root directory and add it to sys.path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

### Directories ###
DATA_DIR = os.path.join(ROOT_DIR, "data")
RESULTS_DIR = os.path.join(ROOT_DIR, "results")

### Files ###
RAW_DATA_CSV = os.path.join(DATA_DIR, "all_epoxy_data.csv")
PREPROCESSED_DATA_CSV = os.path.join(DATA_DIR, "preprocessed_data.csv")

### Constants ###



# Create directories
def make_directories():
    for d in [DATA_DIR,
              RESULTS_DIR]:
        os.makedirs(d, exist_ok=True)


if __name__ == "__main__":
    make_directories()
