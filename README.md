# ajpg Utils

This Python script allows you to unpack and merage ajpg files used in Disney's MMO games.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Use (Guide)](#how-to-use-guide)
- [Usage](#usage)
- [Scripts](#scripts)
- [Credits](#credits)

## Introduction

ajpg is a format used in Disney's MMO games to pack multiple files into a single compressed archive (images). This script allows you to unpack ajpg files and extract the individual files within them. Additionally, it provides functionality to merge p & j files into a images.

## Requirements

- Python 3.x

## Installation

To run the scripts, you might need to install the required Python modules. You can install them using `pip`: ```install pillow lxml```

## How to Use (Guide)

For detailed instructions on how to use the ajpg Utils scripts, refer to the [How to Use (Guide)](HowTo.txt).

## Usage

1. Clone this repository or download the Python script files.

2. Open a terminal or command prompt and navigate to the directory containing the script files.

3. To unpack an ajpg file, run the script: `python ajpg.py`

4. For merging "j" and "p" files, run the script: `python composite.py`

5. Follow the on-screen instructions for providing input paths and options.

## Scripts

### ajpg.py

This script allows you to unpack ajpg files, extracting their contents to individual files. It supports both standalone ajpg files and folders containing multiple ajpg files.

### composite.py

This script enables the merging of "j" and "p" images within corresponding subfolders. It creates merged images with alpha channels, where the merged image filename matches the subfolder name.

## Credits

* [ByteArray](https://github.com/ethanlindley/ByteArray.py) - The ByteArray module used for handling binary data.
* [Original DPak Code Source](https://github.com/rocketprogrammer/DPackUtils) - Source of inspiration for handling .ajpg files.
* creativelynameduser - Helping with [composite.py Script](composite.py)

Feel free to customize this template based on your specific ajpg utility scripts and add any additional information or features as needed.
