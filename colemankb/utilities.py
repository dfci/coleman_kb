__author__ = 'priti'
import re


def remove_white_space(df):
    for col in df.columns:
        try:
            df[col] = df[col].map(lambda x: x.strip())
        except AttributeError:
            continue
    return df


def get_protein_position(aa_pos,var_type ):
    val = re.findall('\d+', aa_pos)
    val = map(int, val)
    if len(val) == 2 and var_type=='INFRAME_INDEL':
        all_pos = range(val[0], val[1]+1)
    else:
        try:
            all_pos = [val[0]]
        except IndexError:
            all_pos = []
    return all_pos


def pathogenicity(anno_df, gene, amino_acid_position, variant_type, exac=''):
    path = []
    anno_gene = anno_df[anno_df['Gene'] == gene]
    anno_gene = anno_gene[anno_gene[variant_type] == 'Y']

    for i, row in anno_gene.iterrows():
        if isinstance(exac, float) and row['EXAC_FREQ'] < exac:
            continue
        if row['AA_MATCH'] == 'NA' and row['AA_START'] == 'NA':
            path.append('p')
        elif row['AA_MATCH'] == amino_acid_position:
            path.append('p')
        elif row['AA_START'] <= amino_acid_position and row['AA_END'] >= amino_acid_position:
            path.append('p')
    if 'p' in path:
        return 'Pathogenic'
    else:
        return 'VUS'
