#! /usr/bin/env python3
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s(%(relativeCreated)6d)[%(threadName)s]%(message)s')

# create a 2x2 Intrepid horizontal curvature tensor field from the A & B complement data, using the formula
# note, the two middle components of Initial are set to NULL
# also note, the raw creation leaving the components as scalar fields, is not given in the examples
from intrepid import intrepid_tasks_pb2 as intrepid
from intrepid import mastertask_pb2 as master
from intrepid.utils import Executor
from intrepid.commontaskmodel_pb2 import DataType as dt
from intrepid.commontaskmodel_pb2 import CoordinateReferenceSystem as crs
from intrepid.intrepid_tasks_pb2 import DB_Operations as dbops
from intrepid.intrepid_tasks_pb2 import OperationType as ops

batch = master.BatchJob()
igtask = batch.IntrepidTask.add()
fmgr = igtask.FileManager
fmgr.Action = dbops.CopyTable
fmgr.Input = "./2131_1_AGGFin_32..DIR"
fmgr.Output = "./2131_1_AGGFin_32_HCTensor..DIR"

igtask = batch.IntrepidTask.add()
dbedit = igtask.dbedit
act = dbedit.Action.add()
act.Type = ops.OpenField
act.Name = "2131_1_AGGFin_32_HCTensor..DIR"

act = dbedit.Action.add()
act.Type = ops.CreateField
act.Dtype = dt.DT_TENSOR
act.Name = "HCTensor_2p2"
act.Initial = "newTensor(A_UV_2p2,A_NE_2p2,Null,Null,B_NE_2p2,B_UV_2p2)"
act.CoordinateSystemType = crs.NED

logging.info("Task:\n%s", batch.__str__())

Executor.execute(batch)
