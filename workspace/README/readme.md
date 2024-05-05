## Sparse New Encodings
This repo runs new encodings (Huffman and Delta) in the example files to compare against existing sparseloop encodings. 

### Other modified repos
In order to add new encodings to sparseloop, other parts of the timeloop/accelergy infrastructure had to be modified. Please see below for a list of modified repos and their changes.

`timeloop`: Added two new format models at timeloop/src/workload/format-models: `delta-encoding.cpp` and `huffman-encoding.cpp`. These files decribe the approximate bit workload expected when using these encodings. Corresponding header files added at timeloop/include/workload/format-models. Other files in timeloop were modified to accept these new classes in addition to the existing ones. Repo can be found here: https://github.com/alkeirn/timeloop 

`timeloopfe`: Minor modifications to timeloopfe/timeloopfe/v4/sparse_optimizations.py to include new encodings. Repo can be found here: https://github.com/alkeirn/timeloopfe

`accelergy-timeloop-infrastructure`: Modifications to swap out git submodules with new repos. Repo can be found here: https://github.com/alkeirn/accelergy-timeloop-infrastructure

`timeloop-acclergy-pytorch`: Changed to use the new timeloop-accelergy-infrastructure repo. Repo can be found here: https://github.com/mk314k/timeloop-accelergy-pytorch

These repos were used to make a new docker image of timeloop and accelergy, which can be pulled by this repo to run the new encoding styles. Docker image found here: https://hub.docker.com/r/kartikesh314/accelergy-timeloop-infrastructure

## Accelergy-Timeloop Infrastructure
This docker aims to provide an experimental environment for easy plug-and-play of examples that run on the accelergy-timeloop DNN accelerator evaluation infrastructure. 

### System Setup
Inside this docker you can find the source files of all necessary setups:
- accelergy: the energy estimation backend 
- timeloop: the mapping exploration frontend
- accelergy-cacti-plug-in: SRAM estimation plug-in
- accelergy-aladdin-plug-in: 45nm component plug-in
- accelergy-table-based-plug-in: entry point for creating your own table-based plug-ins
They are already built/installed and ready to run!

### How to use the docker
- Check if you can run the necessary commands below, i.e., you should not see `command not found` message
    - accelergy
    - accelergyTables
    - cacti
    - timeloop-mapper
    - timeloop-model
    
- Get some examples running!
    - You can clone example repos that we provide to you to your docker folder (available example repos can be found in the example repo readme)
    - You can create your own models (if you already know the tools)

Note, to skip this intro:
```touch ~/.nointro```