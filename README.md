# pydem

PyDEM is a command-line tool that creates digital elevation model .obj files from specified long-lat coordinates.
PyDEM also creates an associated .tiff file to be used as a texture.

Currently, no .mtl file is created.  In the future, this is planned.

PyDEM uses elevation and landsat data from `https://data.worldwind.arc.nasa.gov`.

## Usage

First, install the dependencies in requirements.txt, `numpy`, `scipy` and `utm`.  

`pip install -r requirements.txt`

Then run `dem.py` with the arguments:

`python3 dem.py <MIN_LONG> <MIN_LAT> <MAX_LONG> <MAX_LAT> <RESOLUTION>` or just `python3 dem.py default` for a demo example.

## Troubleshooting

### HTTP Error 400: Bad Request

This likely means your coordinate range was too large for the WMS database to handle.
