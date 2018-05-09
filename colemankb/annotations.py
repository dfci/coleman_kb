__author__ = 'priti'
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import os
import sys
import logging
import datetime as dt
import pandas as pd
import re

import utilities

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class ColemanKB:

    def __init__(self):

        self.google_doc_credentials = 'data/google_credentials.json'
        self.annotation_file = ''
        self.gene = ''
        self.protein_change = ''
        self.variant_type = ''
        self.exac = ''
        self.df = None

    def get_annotation_df(self):
        anno_df = pd.read_csv(self.annotation_file, sep='\t')
        anno_df = utilities.remove_white_space(anno_df)
        anno_df= anno_df.fillna('NA')
        return anno_df

    def annotate_variant(self):
        path_all = []
        path_final = 'VUS'

        if self.df is None:
            self.connect_spreadsheet()

        amino_acid_pos = utilities.get_protein_position(self.protein_change, self.variant_type)
        if len(amino_acid_pos) == 0 or amino_acid_pos[0] == []:
            path_final = utilities.pathogenicity(self.df, self.gene, '', self.variant_type, self.exac)
        else:
            for aa in amino_acid_pos:
                path = utilities.pathogenicity(self.df, self.gene, aa, self.variant_type, self.exac)
                path_all.append(path)
            if 'Pathogenic' in path_all:
                path_final = 'Pathogenic'

        return path_final

    def connect_spreadsheet(self):
        if self.df is not None:
            return
        try:
            json_key = json.load(open(self.google_doc_credentials))
        except IOError:
            logging.error('Cannot find Google doc credential file')
            sys.exit()

        scope = ['https://spreadsheets.google.com/feeds']
        credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
        gc = gspread.authorize(credentials)

        # Open the Registration Spreadsheet
        sh = gc.open("RHP-dynamic-annotation")
        worksheet = sh.get_worksheet(0)

        # Get all Records
        all_data = worksheet.get_all_records()
        self.df = pd.DataFrame(all_data)


