## Overview

RHP KB Api returns pathogenecity status of a variant based on rules defined here:  https://docs.google.com/spreadsheets/d/1xZWM2oTDntcLY9GkwoKPIHK4exlzJQGJ6i3OPMMbowg/edit#gid=0

### Installation
###### 1) clone repository
`git clone THIS-REPO`

###### 2) create virtual environment
```bash
virtualenv ENV-NAME
. ENV-NAME/bin/activate
cd coleman_kb
```

###### 3) install dependencies
`pip install -r requirements.txt`

###### 5) Run the app
python app.py

###### 5) Test on Browser
http://localhost:4848/annotate?gene=BRAF&protein_change=V600E&variant_type=MISSENSE
http://localhost:4848/annotate?gene=CEBPA&protein_change=V600E&variant_type=INFRAME_INDEL&exac=0.0001
http://localhost:4848/annotate?gene=CEBPA&protein_change=V600E&variant_type=INFRAME_INDEL&exac=0.005
