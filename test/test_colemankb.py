__author__ = 'priti'
from colemankb.annotations import ColemanKB
from colemankb.annotations import utilities
s = ColemanKB()
s.connect_spreadsheet()

def test_annotate_variant():    
    s.protein_change = 'V600E'
    s.variant_type = 'MISSENSE'
    s.gene = 'BRAF'
    s.exac = ''
    tier = s.annotate_variant()
    assert tier == 'Pathogenic'

    s.protein_change = 'V602E'
    s.variant_type = 'MISSENSE'
    s.gene = 'BRAF'
    s.exac = ''
    tier = s.annotate_variant()
    assert tier == 'VUS'
    
    s.protein_change = 'V350E'
    s.variant_type = 'NONSENSE'
    s.gene = 'ASXL1'
    s.exac = ''
    tier = s.annotate_variant()
    assert tier == 'Pathogenic'

    s.protein_change = 'V349E'
    s.variant_type = 'NONSENSE'
    s.gene = 'ASXL1'
    s.exac = ''
    tier = s.annotate_variant()
    assert tier == 'VUS'

    s.protein_change = 'V300E'
    s.variant_type = 'MISSENSE'
    s.gene = 'GATA2'
    s.exac = 0.001
    tier = s.annotate_variant()
    assert tier == 'Pathogenic'
    
    s.protein_change = 'V300E'
    s.variant_type = 'MISSENSE'
    s.gene = 'GATA2'
    s.exac = 0.03
    tier = s.annotate_variant()
    assert tier == 'VUS'

    s.protein_change = 'V300E'
    s.variant_type = 'MISSENSE'
    s.gene = 'GATA2'
    s.exac = 0.03
    tier = s.annotate_variant()
    assert tier == 'VUS'

def test_get_protein_position():
    protein_change = '596_601insEYEYDL'
    variant_type = 'INFRAME_INDEL'
    aa = utilities.get_protein_position(protein_change, variant_type)
    assert 599 in aa
    assert 601 in aa
    
    protein_change = 'V600E'
    variant_type = 'MISSENSE'
    aa = utilities.get_protein_position(protein_change, variant_type)
    assert 600 in aa
