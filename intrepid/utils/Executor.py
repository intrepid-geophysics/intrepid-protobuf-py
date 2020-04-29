import argparse
import os
import logging
import subprocess
import sys
import tempfile

from pathlib import Path

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s(%(relativeCreated)6d)[%(threadName)s]%(message)s')

def execute(batch, wd=Path(os.getcwd())):
    logging.info("Executable: %s", exec)
    temp = tempfile.NamedTemporaryFile(mode='w+t', suffix=".task", delete=False)
    logging.info("Temporary taskfile: %s", temp.name)
    logging.info("CWD: %s", wd.as_uri())
    try:
        lines = batch.__str__()
#       logging.info("Task:\n%s", lines)
        temp.writelines(lines)
    finally:
        temp.close()
    penv =  os.environ.copy()
    proc = subprocess.Popen(["fmanager", "-batch", temp.name], cwd=wd, env=penv)
    proc.communicate()
    logging.info("Process #%d returned %d", proc.pid, proc.returncode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a taskfile')
    parser.add_argument('--batch', metavar='N', type=str, nargs='+', help='taskfile list')
    args = parser.parse_args()
