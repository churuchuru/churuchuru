# Churu Churu

## Setup

Install new conda environment
```
conda create --name py3.12 python=3.12 -c conda-forge
```

Install reflex
```
pip install reflex
```

Make new project
```
mkdir my_app_name
cd my_app_name
reflex init
```

## Running

Run application in development mode
```
reflex run
```

If you restart in a new environment, clone the repo, and run
```
reflex init
reflex run
```

Debugging
```
reflex run --loglevel debug
```

## Useful Links
[reflex docs](https://reflex.dev/docs/getting-started/installation/)