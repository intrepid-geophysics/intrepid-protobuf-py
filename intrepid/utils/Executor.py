#! /usr/bin/env python3
import argparse
import os
import logging
import subprocess
import sys
import tempfile

from pathlib import Path

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s(%(relativeCreated)6d)[%(threadName)s]%(message)s')

def execute(batch, wd=Path(os.getcwd()),forceGUI=None):
    """Execute the batch object passed.
    Typically this will be done by passing the batch object into a temporary file and executing using fmanager. By this method fmanager can choose which tool to utilise.
    Alternative executors could be written that are tool specific, or designed for parallel/bulk-batch processing.

    Args:
        batch (Protobuf Object): The populated object created from a master.BatchJob()
        wd (path, optional): Path to the desired working directory. Defaults to Path(os.getcwd()).
        forceGUI (Boolean, optional): Required to be True for 3DExplore visualisations.   Set to True if you wish to force the process/task to the GUI, for debugging or visualisation purposes. Defaults to None.
    """    
    logging.info("Executable: %s", exec)
    if forceGUI:
        temp = tempfile.NamedTemporaryFile(mode='w+t', suffix=".task", delete=False, dir=wd)
    else:
        temp = tempfile.NamedTemporaryFile(mode='w+t', suffix=".task", delete=False)
    logging.info("Temporary taskfile: %s", temp.name)
    logging.info("CWD: %s", wd.as_uri())
    try:
        lines = batch.__str__()
        logging.info("Task in executor:\n%s", lines)
        temp.writelines(lines)
    finally:
        temp.close()
    penv =  os.environ.copy()
    if forceGUI:
        proc = subprocess.Popen(["fmanager", "-default", temp.name], cwd=wd, env=penv)
    else:
        proc = subprocess.Popen(["fmanager", "-batch", temp.name], cwd=wd, env=penv)
    proc.communicate()
    logging.info("Process #%d returned %d", proc.pid, proc.returncode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a taskfile')
    parser.add_argument('--batch', metavar='N', type=str, nargs='+', help='taskfile list')
    args = parser.parse_args()
