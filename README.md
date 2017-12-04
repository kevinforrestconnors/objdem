# objDEM

objDEM is a command-line tool that creates digital elevation model .obj files from specified long-lat coordinates.
objDEM also creates an associated .tiff file to be used as a texture.

Currently, no .mtl file is created.  In the future, this is planned.

objDEM uses elevation and landsat data from `https://data.worldwind.arc.nasa.gov`.

## Usage

First, install the dependencies in requirements.txt, `numpy`, `scipy` and `utm`:

`pip install -r requirements.txt`

Then run **python3** on `objdem.py` with the arguments:

`python objdem.py <MIN_LONG> <MIN_LAT> <MAX_LONG> <MAX_LAT> <RESOLUTION>` or just `python dem.py default` for a demo example.

## Troubleshooting

### HTTP Error 400: Bad Request

This likely means your coordinate range was too large for the WMS database to handle.
