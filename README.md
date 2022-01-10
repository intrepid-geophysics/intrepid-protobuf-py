## Build
python setup.py sdist

## Install and Upgrade (recommended)
With both Python 3+ and pip installed and located on system path, run the command.

```pip install --upgrade git+https://github.com/intrepid-geophysics/intrepid-protobuf-py.git```


## Install and Upgrade (Alternative)
*We cannot guarantee or support all variations of Python environments, Intrepid Geophysics reccomends a Python installation from https://www.python.org/downloads/*

Some users may have non-vanilla installation of Python such as Anaconda.
In all cases you require that the Intrepid-protobuf library is installed to the correct environment, and this environment is accessible from the command window spawned by Intrepid.

in the case of Anaconda, open your Anaconda environment (command prompt) and:

```pip install --upgrade git+https://github.com/intrepid-geophysics/intrepid-protobuf-py.git```

Then, add the python.exe to your system Path, to find it's location open Anaconda Prompt and run the command:

```where python```

## Running your first script
With the library succesfully installed to the Python environment that you have on system Path, use the Intrepid Project Manager to navigate to your working directory containing your python file (examples are included in Intrepid Shipment) open a Command Window using the Project Manager main menu > File > New Command Window, and run your script using python <filename.py>

## Uninstall
```pip uninstall intrepid-protobuf```
