import act
import numpy as np
import xarray as xr
from unc_func import *

def calculate(obj, inst=None, variables=None):

    if inst is None:
        if 'platform_id' in obj.attrs:
            inst = obj.attrs['platform_id']
        elif 'dod_version' in obj.attrs:
            inst = obj.attrs['dod_version'].split('-')[0]
        else:
            raise ValueError('Instrument not defined in dataset')

    if variables is None:
        variables = list(obj.keys())


    inst_unc = {
        'met': run_met
    }
    result = inst_unc[inst](obj, variables)


    return obj
