import xarray as xr


def add_uncert_variable(obj, v, data):
    new_name = v + '_uncertainty'
    atts = {'long_name': 'Vendor uncertainty of '+v}
    if 'units' in obj[v].attrs:
        atts['units'] = obj[v].attrs['units']
    obj[new_name] = xr.DataArray(data=data, attrs=atts, dims=obj[v].dims)

    return obj
