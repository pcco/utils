# PCCO Utils

Utility scripts for PCCO ministry work

## Project Structure

```
root  
├── docker  
├── pcco  
└── scripts  
```

### docker

Contains dockerfiles to build custom docker images

See [docker/README.md](./docker/README.md) for more details

### pcco

Contains the main python package of miscellaneous utilities. In the `pyproject.toml`,
the `project.scripts` section shows available scripts.
After installing the package, you can run the scripts with `-h` to get a help context menu.
If you have shell completion, You can start typing `pcco-` and press tab to see available scripts.

Run `pip install .` to install.

For development it is recommended to use virtual environments.

1. `python3 -m venv <virtual env name>`
1. Activate it based on your OS.
1. Run an editable install with `pip install -e .`
   Any changes you make to the source will be reflected when executing the pcco-\* scripts.

### Scripts

These are miscellaneous bash scripts geared towards a Linux system. A potential future consideration is to run these scripts
from inside a docker container for cross compatibility.

See individual script comments for more usage context.
