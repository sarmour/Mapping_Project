mxds = 'test.mxd'
mapfields = 'test.mxd'
print mxds
print mapfields
if type(mxds) is str:
    newmxd = []
    newmxd.append(mxds)
    mxds = newmxd
if type(mapfields) is str:
    newmapfields = []
    newmapfields.append(mapfields)
    mapfields = newmapfields
print mxds
print mapfields
