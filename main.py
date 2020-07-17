import h5netcdf
import numpy as np
from netCDF4 import Dataset, MFDataset
import tables as tb
import xarray as xr

# dir = r'../../Strelka KB/CO2/OCO2/'
dir = r'Chelyabinsk/'
def walktree(top):
    values = top.groups.values()
    yield values
    for value in top.groups.values():
        for children in walktree(value):
            yield children

def retrieve_hdf5_var(input_fileh5, v_n, node_name):
    h5file = tb.openFile(input_fileh5, "r")
    hdf5_object = h5file.getNode(node_name, v_n)
    array = hdf5_object.read()
    h5file.close()
    return array

#f = Dataset(dir + 'oco2_LtCO2_200110_B9003r_200204191136s.nc4', 'r', format="NETCDF4")
f = Dataset(dir + 'oco2_LtCO2_200121_B9003r_200204193452s.nc4', 'r', format="NETCDF4")
#f = MFDataset(dir +'/*.nc4')
#f = xr.open_mfdataset(dir +'/*.nc4')


xco2 = f.variables['xco2']
lon = f.variables['longitude']
lat = f.variables['latitude']
time = f.variables['time']

#print(xco2)

lat_bnds, lon_bnds = [59 , 62], [54 , 56]

lat_inds = np.where((lat[:] > lat_bnds[0]) & (lat[:] < lat_bnds[1]))
lon_inds = np.where((lon[:] > lon_bnds[0]) & (lon[:] < lon_bnds[1]))

inds = np.intersect1d(lat_inds, lon_inds)

xco2_subset = xco2[inds]
lat_subset = lat[inds]
lon_subset = lon[inds]

print(xco2_subset[:])


# for children in walktree(f):
#     print(children)
#     for child in children:
        # print(child.dimensions)
        # print(child.variables)
        # print(child.groups)
        # print(children["/Sounding/xco2"])

# print(f.data_model)
# print(f.variables)

f.close()

# input_fileh5 = 'oco2_LtCO2_200110_B9003r_200204191136s.nc4'
#
# Vars = {}  # Init dictionary
# node_name = "/RetrievalResults"  # Node definition
# v_n = "xco2"  # Variable name
# # Assign to dictionary
# Vars['xco2'] = retrieve_hdf5_var(input_fileh5, v_n, node_name)