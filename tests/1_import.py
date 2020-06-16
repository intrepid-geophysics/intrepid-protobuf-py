#! /usr/bin/env python3
from intrepid import mastertask_pb2 as master
from intrepid import commontaskmodel_pb2 as ctm
from intrepid.commontaskmodel_pb2 import FieldAlias
from intrepid.intrepid_tasks_pb2 import DB_Operations
from intrepid.intrepid_tasks_pb2 import GeophysicsFormatType
from intrepid.utils import Executor

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                    format='%(asctime)s(%(relativeCreated)6d)[%(threadName)s]%(message)s')

# import of the collection of raw marine databases.
# suitable for a next round of gridding, 
# give access to the full range of line database drivers  eg csv, Intrepid, netcdf etc.
# Usage: python 1_import.py

batch = master.BatchJob()

inputs = ["0004",
          "0053",
          "0055",
          "0056an",
          "0096",
          "0097",
          "0101an",
          "0110an",
          "0127an",
          "0128",
          "0136an",
          "0161",
          "0167an",
          "0168a",
          "0174an",
          "1339",
          "1359fd"]

for input in inputs:
    igtask = batch.IntrepidTask.add()
    importTask = igtask.Import
    importTask.ReportFile = "NorthWestShelf_ship_trackimport.rpt"
    importTask.Input = f'${{cookbook}}/Marine_Levelling/Rawdata/{input}.asc_data'
    importTask.Output = f'raw{input}..DIR'
    importTask.Format = GeophysicsFormatType.ASCIICOLUMNS

    asciiColumns = importTask.AsciiColumns

    asciiColumns.FixedLength = False
    asciiColumns.SkipRecords = 0
    asciiColumns.DDF = "${cookbook}/Marine_Levelling/M_TASKS/marine.proto_ddf"
    asciiColumns.StopOnError = True
    asciiColumns.ReportDiagnostics = True

    igtask = batch.IntrepidTask.add()
    fm = igtask.FileManager
    fm.Input = f'raw{input}..DIR'
    fm.Action = DB_Operations.EditSurveyInfo
    fm.Alias_String = "SurveyID"
    fm.Alias_Code = FieldAlias.FA_FLIGHT

    igtask = batch.IntrepidTask.add()
    fm = igtask.FileManager
    fm.Input = f'raw{input}..DIR'
    fm.Action = DB_Operations.EditSurveyInfo
    fm.Alias_String = "Time"
    fm.Alias_Code = FieldAlias.FA_FID

logging.info("\n%s", batch.__str__())

Executor.execute(batch)
