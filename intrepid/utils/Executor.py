import argparse
import os
import logging
import subprocess
import sys
import tempfile

from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s(%(relativeCreated)6d)[%(threadName)s]%(message)s')

from intrepid import commontaskmodel_pb2 as ctm
from intrepid import filter_description_pb2 as fdf
from intrepid import intrepid_tasks_pb2 as intrepid_tasks
from intrepid import mastertask_pb2 as master_tasks

def getExecNameForIntrepidTask(task):
    exec = ""
    # database/ file based operations
    if task.HasField("Import"):
        exec = "import"
    if task.HasField("ExportDB"):
        exec = "export"
    if task.HasField("Subset"):
        exec = "subset"
    if task.HasField("GridOp"):
        exec = "gridopAppGUI"
    if task.HasField("ProjConv"):
        exec = "jprojconv"
    if task.HasField("dbedit"):
        exec = "dbedit"
    # survey/line based tools
    if task.HasField("Dataset_Resampler"):
        exec = "dataset_resampler"
    if task.HasField("SurveyDistance"):
        exec = "sdist"
    if task.HasField("FileManager"):
        exec = "fmanager"
    if task.HasField("ClusterAnalysis"):
        exec = "cluster"
    if task.HasField("Fedit"): # old flight path editor for QA/QC
        exec = "fedit"
    if task.HasField("ClipLine"):
        exec = "clipline"
    if task.HasField("ProfileEdit"): # old flight path editor for QA/QC
        exec = "pedit"
    # spatial grid filtering
    if task.HasField("Convolve"):
        exec = "cfilter"
    if task.HasField("GridFilter"):
        exec = "gfilt"
    if task.HasField("Decorrugate"):
        exec = "decor"
    if task.HasField("MicroLevel"):
        exec = "mlevel"
    if task.HasField("LineFilter"):
        exec = "lfilter"
    if task.HasField("WienerFilter"):
        exec = "wiener"
    # grid interpolators, tools
    if task.HasField("Gridding"):
        exec = "jGridding"
    if task.HasField("Gridmerge"):
        exec = "gridmerge"
    # gravity tools
    if task.HasField("Gravity"):
        exec = "gravity"
    if task.HasField("Terrain_Correction_QuadTree"):
        exec = "terraincorrect"
    if task.HasField("isostatic"):
        exec = "IsostaticCorrectionAppGUI"
    if task.HasField("Levelling"):
        exec = "newlevel"
    if task.HasField("MarineLevel"):
        exec = "MarineLevellingAppGUI"
    if task.HasField("SplitCruise"):
        exec = "MarineSplitAppGUI"
    if task.HasField("GravityMerge"):
        exec = "MergeDataAppGUI"
    # some gamma ray tools
    if task.HasField("Radio256"):
        exec = "mrad256"
    if task.HasField("MaximumNoiseFraction"):
        exec = "mnf256"
    if task.HasField("GamAdj"):
        exec = "gamadj"
    if task.HasField("UraniumLevelling"):
        exec = "ulevel"
    # interpretation stuff
    if task.HasField("Naudy"):
        exec = "naudyd"
    # if task.HasField("MakeHistogram"):
    #    exec = "cfilter"
    if task.HasField("WormE"):
        exec = "worme"
    if task.HasField("Euler"):
        exec = "euler"
    # forward modelling commands
    if task.HasField("ForwardModelFromDykes"): # Horst various dyke methods
        exec = "MTdyke"
    if task.HasField("ForwardModelFromSurfaces"): # facet modelling of closed arbitary volume
        exec = "MTvol"
    if task.HasField("ForwardModelFromLayerCake"):
        exec = "layer_model"
    # misc
    if task.HasField("MapCompExport"):
        if task.MapCompExport().HasField("input"):
            exec = "mapprint"
        else:
            exec = "jMapComp"
    return exec

def getExecNameForMagneticTask(task):
    exec = ""
    return exec

def getExecNameForJetstreamTask(task):
    exec = ""
    return exec

def getExecNameForAEMTask(task):
    exec = ""
    return exec

def getExecNameForIntrepid3DExplore(task):
    exec = ""
    return exec

def getExecNameForPetrelTask(task):
    exec = ""
    return exec

def getExecNameForGeomodellerTask(task):
    exec = ""
    return exec

def getExecNameForInversionTask(task):
    exec = ""
    return exec

def execute(batch, wd=Path(__file__).parent):
    for task in batch.IntrepidTask:
        exec = getExecNameForIntrepidTask(task)
    for task in batch.MagneticTask:
        exec = getExecNameForMagneticTask(task)
    for task in batch.JetstreamTask:
        exec = getExecNameForJetstreamTask(task)
    for task in batch.AEMTask:
        exec = getExecNameForAEMTask(task)
    for task in batch.Intrepid3DExplore:
        exec = getExecNameForIntrepid3DExplore(task)
    for task in batch.PetrelTask:
        exec = getExecNameForPetrelTask(task)
    for task in batch.GeomodellerTask:
        exec = getExecNameForGeomodellerTask(task)
    for task in batch.InversionTask:
        exec = getExecNameForInversionTask(task)
    
    if exec:
        logging.info("Found exec: " + exec)
        temp = tempfile.NamedTemporaryFile(mode='w+t', suffix=".task", delete=False)
        logging.info("Temp file: " + temp.name)
        logging.info("WD: " + wd.as_uri())
        try:
            temp.writelines(str(batch))
        finally:
            temp.close()
        penv =  os.environ.copy()
        subprocess.run([exec, "-batch", temp.name], cwd=wd, env=penv)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a taskfile')
    parser.add_argument('--batch', metavar='N', type=str, nargs='+', help='taskfile list')
    args = parser.parse_args()
