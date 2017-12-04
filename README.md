# objDEM

objDEM is a command-line tool that creates digital elevation model .obj files from specified long-lat coordinates.
objDEM also creates an associated .tiff file to be used as a texture.

Currently, no `.mtl` file is created.  In the future, this is planned.

objDEM uses elevation and landsat data from `https://data.worldwind.arc.nasa.gov`.

## Usage

`objdem <MIN_LONG> <MIN_LAT> <MAX_LONG> <MAX_LAT> <RESOLUTION>` or just `objdem default` for a demo example.

**Important:** files called `dem.obj` and `map.tiff` will be created in your current directory.  This may override existing files with the same name.

## Troubleshooting

### HTTP Error 400: Bad Request

This likely means your coordinate range was too large for the WMS database to handle.
