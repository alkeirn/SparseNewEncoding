## Sparse New Encodings
This repo runs new encodings (Huffman and Delta) in the example files to compare against existing sparseloop encodings. 

### Other modified repos
In order to add new encodings to sparseloop, other parts of the timeloop/accelergy infrastructure had to be modified. Please see below for a list of modified repos and their changes.

`timeloop`: Added two new format models at timeloop/src/workload/format-models: `delta-encoding.cpp` and `huffman-encoding.cpp`. These files decribe the approximate bit workload expected when using these encodings. Corresponding header files added at timeloop/include/workload/format-models. Other files in timeloop were modified to accept these new classes in addition to the existing ones. Repo can be found here: https://github.com/alkeirn/timeloop 

`timeloopfe`: Minor modifications to timeloopfe/timeloopfe/v4/sparse_optimizations.py to include new encodings. Repo can be found here: https://github.com/alkeirn/timeloopfe

`accelergy-timeloop-infrastructure`: Modifications to swap out git submodules with new repos. Repo can be found here: https://github.com/alkeirn/accelergy-timeloop-infrastructure

`timeloop-acclergy-pytorch`: Changed to use the new timeloop-accelergy-infrastructure repo. Repo can be founf here: https://github.com/mk314k/timeloop-accelergy-pytorch

These repos were used to make a new docker image of timeloop and accelergy, which can be pulled by this repo to run the new encoding styles. Docker image found here: https://hub.docker.com/r/kartikesh314/accelergy-timeloop-infrastructure

# Overview
Welcome to `timeloop-accelergy-exercises`! This repository contains tutorials,
exercises, and examples to get you started with Timeloop and Accelergy. In this
directory, you'll find the following.

#### `tutorial_exercises`
This directory contains exercises and tutorials to teach you how to use
Timeloop. Note that exercises 1 and 2 are prerequisites for the rest of the
exercises, and should be completed first.

#### `cheatsheets`
This directory contains YAML syntax examples and explanations for YAML syntax
and parsing, as well as some of the Timeloop input files. They're meant to be
used as a quick reference when writing your own input files.

#### `example_designs`
This directory contains example Timeloop accelerator designs that can be used
and/or adapted to run your own experiments.

#### `timeloop_spec.yaml`
This file contains a full specification of the Timeloop input file format,
including all allowed fields and their types. Use this as a reference when
writing your own Timeloop input files.