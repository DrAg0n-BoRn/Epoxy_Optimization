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

FEATURE_ENG_DIR = os.path.join(DATA_DIR, "Feature Engineering")

MICE_IMPUTED_DATASETS_DIR = os.path.join(DATA_DIR, "MICE Imputed Datasets")
MICE_VIF_IMPUTED_DATASETS_DIR = os.path.join(DATA_DIR, "MICE VIF Imputed Datasets")

MICE_METRICS_DIR = os.path.join(RESULTS_DIR, "MICE")
MODEL_METRICS_DIR = os.path.join(RESULTS_DIR, "Model Metrics")
OPTIMIZATION_RESULTS_DIR = os.path.join(RESULTS_DIR, "Optimization Results")

### Files ###
RAW_DATA_CSV = os.path.join(DATA_DIR, "all_epoxy_data.csv")
PREPROCESSED_DATA_CSV = os.path.join(DATA_DIR, "preprocessed_data.csv")
ENGINEERED_DATA_CSV = os.path.join(DATA_DIR, "engineered_data.csv")

### Constants ###
TARGETS = ["fracture_toughness(MPa*m0.5)",
          "flexural_strength(MPa)",
          "flexural_modulus(MPa)",
          "impact_strength(kJ/m2)",
          "young_modulus(MPa)",
          "tensile_strength(MPa)",
          "shear_strength(MPa)",
          "elongation_at_break(%)"]


# Create directories
def make_directories():
    for d in [DATA_DIR,
              RESULTS_DIR,
              FEATURE_ENG_DIR,
              MICE_IMPUTED_DATASETS_DIR,
              MICE_VIF_IMPUTED_DATASETS_DIR,
              MICE_METRICS_DIR,
              MODEL_METRICS_DIR,
              OPTIMIZATION_RESULTS_DIR]:
        os.makedirs(d, exist_ok=True)


if __name__ == "__main__":
    make_directories()
