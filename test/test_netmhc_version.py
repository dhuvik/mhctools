from nose.tools import raises

from mhctools import NetMHC3, NetMHC4
from mhctools.alleles import normalize_allele_name


def run_class_with_executable(mhc_class, mhc_executable):
    alleles = [normalize_allele_name("HLA-A*02:01")]
    predictor = mhc_class(
        alleles=alleles,
        epitope_lengths=[9],
        program_name=mhc_executable)
    fasta_dictionary = {
        "SMAD4-001": "ASIINFKELA",
        "TP53-001": "ASILLLVFYW"
    }
    epitope_collection = predictor.predict(
        fasta_dictionary=fasta_dictionary)

@raises(SystemError)
def test_executable_mismatch_3_4():
    run_class_with_executable(NetMHC3, "netMHC")

@raises(SystemError)
def test_executable_mismatch_4_3():
    run_class_with_executable(NetMHC4, "netMHC-3.4")
