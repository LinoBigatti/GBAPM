# GBA Palette Manager

A tool to edit and export palettes, to be used on the GBA.

## Getting Started

Follow these instructions to build the tool from source.

### Prerequisites

Install python 3.6.7:

#### Windows

Install from [this releases](https://www.python.org/downloads/windows/).

#### MacOs:

```
brew install python3
```

#### Ubuntu:

```bash
sudo apt-get install python3
```

Install pip for python 3:

#### Windows

It is already part of the python 3 install.

#### MacOs:

It is already part of the python 3 install.

#### Ubuntu:

```bash
sudo apt-get install pip3
```

Then install the required packages:

```
pip3 install fbs PyQt5==5.9.2 PyInstaller==3.4
```

### Running the tool

First, go to the directory where you downloaded the source:

```bash
cd /path/to/source/
```

And run it trough fbs:

```bash
fbs run
```

You can also freeze it to have an executable:

```bash
fbs freeze
```

## Built With

* [Python](https://www.python.org/) - The lenguage used to build the tool.
* [PyQt](https://riverbankcomputing.com/software/pyqt/intro) - The library used for the GUI.
* [Fbs](https://build-system.fman.io/) - The build system.

## Authors

* **Lino Bigatti** - *Main tool coder.*
