# QGreenland

This project uses a `luigi` pipeline to generate the QGreenland package. This
project is currently in early development stages, so expect rapid change.
Nothing is written in stone! Releases can be found at
https://qgreenland.org/explore!


## Configuration

There are 3 configuration files; `layers.yml` is the important one. It references
the others.


### Layers

Each element represents a QGIS layer.


### Layer groups

Each element represents a QGIS layer group. Keep in mind that the first layer's
group will always be automatically selected and expanded.


### Datasets

A dataset isn't necessarily a dataproduct, but it might be. A dataset is any
collection of data representing some measurement, hosted anywhere. Current
access methods include `cmr` (by `granule_ur`s) and `http` (by `url`s).


## Pipeline

As of `v0.6.0`:

* Build layers:
    * Coastlines
        * Fetch
        * Unzip
        * Reproject (EPSG:3411)
        * Subset (QGreenland project extent)
    * Arctic DEM
        * Fetch
        * Reproject (EPSG:3411)
        * Subset (QGreenland project extent)
    * IceBridge BedMachine
        * Fetch
        * For each dataset (bed, thickness, surface):
            * Extract dataset
            * Reproject (EPSG:3411) and resample (1km)
* Generate .qgs project file including all layers.
* Create zip file with version in filename, e.g. `QGreenland_v0.6.0.zip`.

NOTE: The full pipeline will not always be enumerated here; just a
representative sample.


## Running the project

The project is run as a docker container stack. It runs Luigi (with visualizer
at port 8082) as a service for running tasks, as well as NGINX for hosting
outputs.

In order to download data behind Earthdata Login, you must provide the
following environment variables on the docker host:

* `EARTHDATA_USERNAME`
* `EARTHDATA_PASSWORD`

Developers at NSIDC may use the values stored in Vault at the following path:
`nsidc/apps/qgreenland`. Those outside of NSIDC must use their personal
Earthdata Login credentials. New users to Earthdata can register here:
https://urs.earthdata.nasa.gov/users/new


### Starting the stack locally

Populate the environment variables with the `export` command, then bring up the
stack:

```
cd luigi
docker-compose up -d
```

### Starting a Luigi pipeline

```
cd scripts/
. run_task.sh
```

The `run_task.sh` script is built to run the entire pipeline. From its example,
you can run individual layer pipelines, e.g.:

```
docker-compose exec luigi \
  luigi --module qgreenland.tasks.layers \
  BedMachineDataset --dataset-name=bed
```

See the [Luigi documentation](https://luigi.readthedocs.io/en/stable/running_luigi.html)
for more information on running Luigi from the CLI.


#### Debugging a Luigi pipeline

Simply put `breakpoint()` anywhere in the pipeline code, then use `scripts/run_task.sh` (ensure worker count is `1`).


## Contributing

You can contribute to this project even if you don't have write access by
forking, making your change, making all tests pass, then opening a Pull
Request.

Changes to layer styles can be done without editing Python code.


### Contributing styles

You can contribute style changes without editing any Python code using the
following process:

* Download (or build) and open the most recent version of the project in QGIS.
* In the 'Layers' menu, double click on the layer you wish to edit.
* Open the 'symbology' tab.
* Make your desired style changes.
* In the lower-left corner, click the 'Style' dropdown.
* In this menu, select 'Save Style...'

![Save style](docs/images/save_style.png)

* At this point, if you're uncomfortable with Git and GitHub, you can email us
  your style file at qgreenland.info@gmail.com. Otherwise, continue on...
* Save the style to `qgreenland/assets/styles/<name>.qml` directory of this
  repository. Keep in mind that styles can be shared between layers, so give
  the style a generic name instead of a layer-specific name where possible.
* Edit the `qgreenland/layers.yml` file and find the layer(s) you wish to apply
  this style to. Populate the `style` key for each layer with the name of the
  `.qml` file you saved in the previous step, excluding the extension. For
  example, if you saved `foo.qml`, then populate `style: 'foo'`.

![Style in YAML](docs/images/style_in_yaml.png)


### Contributing metadata

Metadata for a layer can be set in the `qgreenland/layers.yml` configuration
file, under the `metadata` key for the layer in question. For example, metadata
for the `coastlines` layer may look like the following:

```
coastlines:
  metadata:
    title: 'Natural Earth Coastlines'
    abstract:
      text:  'Natural Earth Coastlines (Public Domain)'
      citation:
        text: 'Made with Natural Earth'
        url: 'https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md'
```

The metadata section defines the values that get used to create the on-hover
popup text that is shown when a user hovers their cursor over a layer in the
table of contents in QGIS. Additionally, these values are used to set the fields
in the metadata section of the layer's properties` popup.

The final abstract text shown in QGIS is a combination of the values under the
`abstract` key. In the above example, the abstract text would become:

```
Natural Earth Coastlines (Public Domain)

Citation:
Made with Natural Earth

Citation URL:
https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md
```

Note:

It is possible to export metadata from the QGIS GUI to an xml-formatted `.qmd`
file. If collaborators wish to define metadata through the QGIS GUI, support for
ingesting `.qmd` files may be implemented in the future.


### Contributing new layers

Add a new class to `qgreenland/tasks/layers.py` for your new layer. Compose
Luigi tasks to build your final QGreenland layer following the example of other
layers.

TODO: Flesh this out more.


## Releasing

Currently there is no automated release process. The manual process is:

When developing, increment the proper version part (`major`, `minor`, `dev`)
with the `version.bump {part}` invoke task. For example, to bump the minor
version:

```
invoke version.bump minor
```

This will automatically add the `dev` tag to the end of the version string if
one does not already exist. For example, if bumping the minor version from
`v1.1.1`, the version will become `v1.2.1dev`.

To release, invoke the `version.bump` tag with the `release` part:

```
invoke version.bump release
```

This will remove the `dev` part from the version. For example, using the
`release` part on `v1.2.1dev` will change the version to `v1.2.1`.


# Troubleshooting

## QGIS won't start on OSX Catalina

QGIS is currently not "notarized" for Mac OSX. If you receive `The developer of this app needs to update it to work with this version of macOS. Contact the developer for more information.`, then, in your OSX menus, try:

- "Security and Privacy"
- "Allow apps downloaded from..."
- "App Store and identified developers"
- Locate QGIS here and select "Open anyway"
