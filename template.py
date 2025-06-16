from pathlib import Path
import os

list_of_files = [
".github/workflows/.gitkeep",
"src/init.py",
"src/components/init.py",
"src/components/data_ingestion.py",
"src/components/data_transformation.py",
"src/components/model_trainer.py",
"src/components/model_evaluation.py",
"src/pipeline/init.py",
"src/pipeline/training_pipeline.py",
"src/pipeline/prediction_pipeline.py",
"src/utils/init.py",
"src/utils/utils.py",
"src/logger/logging.py",
"src/exception/exception.py",
"tests/unit/init.py",
"tests/integration/init.py",
"init_setup.sh",
"requirements.txt",
"requirements_dev.txt",
"setup.py",
"setup.cfg",
"pyproject.toml",
"tox.ini",
"experiment/experiments.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent

        # Create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
     

    # Create empty file if it doesn't exist or is empty
    if (not filepath.exists()) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # create an empty file