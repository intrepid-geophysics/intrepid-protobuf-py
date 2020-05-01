#! /usr/bin/env python3
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s(%(relativeCreated)6d)[%(threadName)s]%(message)s')

# example of an airborne survey where some of the flight lines get too close to each other
# when gridded, the output contains "tares" that detract
# use this tool to clean up parts of a survey that are "over constrained" and show errors.
# changes X/Y alias
from intrepid import mastertask_pb2 as master
from intrepid.intrepid_tasks_pb2 import DB_Operations

from intrepid.utils import Executor

batch = master.BatchJob()
igtask = batch.IntrepidTask.add()
fmgr = igtask.FileManager
fmgr.Action = DB_Operations.CopyTable
fmgr.Input = "${tutorial}/Intrepid_datasets/EBA_DBs/ebagoola_S..DIR"
fmgr.Output = "./ebagoola_S..DIR"

igtask = batch.IntrepidTask.add()
clip_line = igtask.ClipLine
clip_line.InputFile = "ebagoola_S..DIR"
clip_line.X = "x"
clip_line.Y = "y"
clip_line.LineType = "linetype"
clip_line.Xout = "E_Clip"
clip_line.Yout = "N_Clip"
clip_line.MinimumSeparation = 200.0
clip_line.MinimumSegmentLength = 50

logging.info("\n%s", batch.__str__())

Executor.execute(batch)
