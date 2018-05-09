import os
import sys
import json
import logging

DATAHUB_PATH = ""

# check that secrets file exists
file_path = os.getenv("SECRETS_JSON", None)
if file_path is None:
    logging.error("ENVAR SECRETS_JSON not set")
    sys.exit(1)

# pull values.
with open(file_path) as fin:
    vars = json.load(fin)
    for name, value in vars.iteritems():
        setattr(sys.modules[__name__], name, value)

