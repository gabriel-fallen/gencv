# GenCV

Generate a series of CVs from data (JSON) files.

The tool generates subfolders in the `dist` folder named the same as the data
files (JSON files in the `data` folder). In every subfolder it creates an HTML
CV file with a name of the form `firstname lastname.html`. The first and the last
names are extracted from a data file. Thus `firstname` and `lastname` are mandatory
fields while the rest are optional.

I personally convert the CVs into PDF using "save to PDF" feature of my browser. :)


## Setup

Usual local Python project installation with a virtual environment.

```sh
$ python -m venv venv
$ venv/Scripts/activate
$ pip install -r requirements.txt
```

## Running

```sh
$ python generate.py
```

## Roadmap

Version 0.4
- [ ] Move work experience to JSON

Version 0.6
- [ ] JSON partials

Version 0.8
- [ ] Interactive infographic CV

Version 1.0
- [ ] Better data format
