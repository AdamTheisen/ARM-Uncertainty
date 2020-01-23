import act
import numpy as np
import xarray as xr

def run_met(obj, variables):
    for v in variables:
        if v == 'temp_mean':
            uncert=[0.5, 0.2, 0.4]
            temp=[-40., 20., 60.]
            data = np.interp(obj[v].values, temp, uncert)
        else:
            continue

        obj = add_uncert_variable(obj, v, data)
  
    return obj

def add_uncert_variable(obj, v, data):
    new_name = v + '_uncertainty'
    atts = {'long_name': 'Vendor uncertainty of '+v}
    if 'units' in obj[v].attrs:
        atts['units'] = obj[v].attrs['units']
    obj[new_name] = xr.DataArray(data=data, attrs=atts, dims=obj[v].dims)

    return obj

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
