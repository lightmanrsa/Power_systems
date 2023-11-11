# run_study.py

"""This script is necessary for using subprocessing. In \power-system-tools\interface_tools\gui_classes\widget_classes.py,
the line subprocess.run([INTERPERTER_PATHS[script_type], r'run_study.py', self.project_id, script_type, study], check=True) effectively
runs this script as if from the command line. the parameters project_id, study_type, and study are passed as if they were command
line arguments. This is necessary to accomodate software APIs requiring different Python interperters."""

import sys
import importlib
import datetime
import os
import logging

import interface_tools.gui_classes.widget_classes as wc
import interface_tools.project_manager.project_management as pm


def run_study(project_id: str, study_script: str, study_name: str) -> None:
    """This function is run to allow the use of modeules in PS software's test_scripts directories as subprocesses. Modules in the test_scripts directories are imported dynamically.

    Args:
        project_id (str): The id of the project
        study_script (str): This is the module to import. It will be in form 'software_tools.[SOFTWARE]_tools.test_scripts.{study_script}.py'
        study_name (str): The name of the function in the study_script to be run.
    Returns:
        None
    """
    study_module = importlib.import_module(
        study_script
    )  # Dynamically import module based on the study to be run
    study_function = getattr(
        study_module, study_name
    )  # Get the function in the imported module to be run
    study_function(project_id)  # ALL PSSE studies take project_id as a argument


if __name__ == "__main__":
    project_id = sys.argv[1]
    study_script = sys.argv[2]
    study_name = sys.argv[3]
    this_proj = pm.Project(project_id)
    logs_path = os.path.join(this_proj.output_dir, "logs")
    if not os.path.exists(logs_path):
        os.mkdir(logs_path)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    now = datetime.datetime.now()
    date_time_prefix = now.strftime("%Y%m%d_%H%M")
    path = os.path.join(logs_path, f"{date_time_prefix}_{study_script}.log")
    file_handler = logging.FileHandler(path)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    # Add the file handler to the logger
    logger.addHandler(file_handler)
    run_study(project_id, study_script, study_name)
    logger.removeHandler(
        file_handler
    )  # Remove the file handler so it doesn't interfere with the nextfunction
    sys.exit()
