import os, shutil
import json
import chevron


# FIXME: make into parameters/args
SRC_DIR  = "src"    # where to look for HTML template(s)
DATA_DIR = "data"   # where to look for JSON files with data
DATA_EXT = ".json"  # might want to change to '.json.mustache' in the future
DIST_DIR = "dist"   # where to make folders with resulting CVs
HTML_TEMPLATE = "index.html"
STYLE_FILE    = "style.css"

data_file_names = [os.path.splitext(fname)[0] for fname in os.listdir(DATA_DIR) if os.path.splitext(fname)[1] == DATA_EXT]

with open(os.path.join(SRC_DIR, HTML_TEMPLATE), 'r') as t:
  template = t.read()

for cvname in data_file_names:
  # first make a subdir
  cv_dir = os.path.join(DIST_DIR, cvname)
  os.makedirs(cv_dir, exist_ok=True)

  data_name = os.path.join(DATA_DIR, cvname + DATA_EXT)
  with open(data_name, "r") as data_file:
    data = json.load(data_file)

    args = {
      'template': template,
      'data': data,
      # TODO: path to partials
    }
    cv = chevron.render(**args)

    first_name = data["first_name"]
    last_name  = data["last_name"]
    dist_file  = f"{first_name} {last_name}.html"
    with open(os.path.join(cv_dir, dist_file), "w") as cv_file:
      cv_file.write(cv)

    # and copy CSS file
    shutil.copy(os.path.join(SRC_DIR, STYLE_FILE), cv_dir)

