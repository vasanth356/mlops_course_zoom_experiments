
#question1
import mlflow
print("MLflow Version:", mlflow.__version__)

# question2

import os
output_folder = "./output"
num_files = len(os.listdir(output_folder))
print(f"Number of files in {output_folder}: {num_files}")


# Q3. Train a model with autolog


