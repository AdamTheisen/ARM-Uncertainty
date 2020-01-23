import numpy as np
from . import utils


def run_met(obj, variables):
    for v in variables:
        if v == 'temp_mean':
            uncert=[0.5, 0.2, 0.4]
            temp=[-40., 20., 60.]
            data = np.interp(obj[v].values, temp, uncert)
        else:
            continue

        obj = utils.add_uncert_variable(obj, v, data)

    return obj
