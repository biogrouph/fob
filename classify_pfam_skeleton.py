#!/usr/bin/python

import urllib2
import xml.etree.ElementTree as ET
import argparse
import itertools


def retrieve_pfam_data(uniprot_id):
    """
    For each protein, retrieve Pfam data.
    :param uniprot_id: UniProt ID of the protein.
    :return: Pfam data corresponding to that protein in xml format.
    """
    url = "http://pfam.xfam.org/protein/" + uniprot_id.strip() + "?output=xml"

    fh = urllib2.urlopen(url)
    result = fh.read()
    fh.close()
    return result


def save_pfam_response(pfam_data, output_file):
    """
    Saves the pfam response to xml file.
    :param pfam_data: the response from the server.
    :param output_file: the output file for saving the response.
    """
    ##########################
    ### START CODING HERE ####
    ##########################
    pass
    ##########################
    ###  END CODING HERE  ####
    ##########################


def parse_pfam_xml(pfam_response_xml):
    """
    Parse the xml data from Pfam response.
    :param pfam_response_xml: an xml file corresponding to a protein ID extracted from Pfam database.
    :return: a dictionary containing the protein UniProtID (key) and as value a list
             containing the Pfam family/motif/domain's accession number it belongs to
             and the level of curation (Pfam-A or Pfam-B).
    """
    ##########################
    ### START CODING HERE ####
    ##########################
    
    ##########################
    ###  END CODING HERE  ####
    ##########################


def compute_similarity_score(prot1_pfam, prot2_pfam):
    """
    Computes the score for two proteins on the basis of the data from Pfam database.
    :param prot1_pfam: data for protein 1 from Pfam.
    :param prot2_pfam: data for protein 2 from Pfam.
    :return: similarity score (float)
    """
    ##########################
    ### START CODING HERE ####
    ##########################
    # You need to decide whether you need this function for Pfam database.
    pass
    ##########################
    ###  END CODING HERE  ####
    ##########################


def check_similarity_for_protein_pair(pror1_pfam, prot2_pfam):
    """
    Returns the similarity score between two proteins.
    :param pror1_pfam: pfam family/motif/domain's accession number the protein 1 belongs to
                    and the level of curation (Pfam-A or Pfam-B).
    :param pror2_pfam: pfam family/motif/domain's accession number the protein 1 belongs to
                    and the level of curation (Pfam-A or Pfam-B).
    :return: "different", "similar" or "ambiguous".
    """
    ##########################
    ### START CODING HERE ####
    ##########################

    ##########################
    ###  END CODING HERE  ####
    ##########################

# If you will use the numeric score for Pfam (similar to GO), you may want to use check_similarity_for_protein_pair
# with other arguments. See the example below.
# def check_similarity_for_protein_pair(score, threshold):
#    pass


def assign_homology(pfam_data, protein_pairs):
    """
    :param pfam_data: a dictionary containing protein Uniprot IDs (keys) and the Pfam data for them(values)
    :param proteins_pairs: a file containing all protein pairs to compare
    :return: a dictionary with all protein pairs (keys) and their similarity - different/similar/ambiguous (values)
    """
    pfam_homology = dict()
    ##########################
    ### START CODING HERE ####
    ##########################

    ##########################
    ###  END CODING HERE  ####
    ##########################
    return pfam_homology


def generate_all_possible_protein_pairs(protein_ids):
    """
    Returns a list containing all unique protein pairs.
    :param protein_ids: list of all proteins IDs.
    :return: list of possible unique protein pairs.
    """
    pairs = list()
    ##########################
    ### START CODING HERE ####
    ##########################
    # You can add a pair of proteins to the list using the following code:
    # pairs_list.append((protein1, protein2))
    # Generate all possible combinations of IDs
  
    ########################
    ### END CODING HERE ####
    ########################
    return pairs


def read_protein_ids_file(filename):
    """
    Returns the list of UniProt IDs contained in the input file.
    :param filename:
    :return: list of UniProt IDs in the input file.
    """
    ##########################
    ### START CODING HERE ####
    ##########################

    #######################
    ### END CODING HERE ###
    #######################
    return protein_ids


def write_output(pfam_homology, output_file):
    """
    Writes in an output file the all of the protein pairs and their similarity/dissimilarity.
    :param pfam_homology: a dictionary with all protein pairs (keys) and
    their similarity - different/similar/ambiguous (values).
    :param output_file: the name of the output file.
    """
    with open(output_file, "w") as f:
        for pair, homology in pfam_homology.iteritems():
            f.write("\t".join([pair[0], pair[1], homology]) + "\n")


def main(protein_ids_file, output_file):
    ##########################
    ### START CODING HERE ####
    ##########################

    #######################
    ### END CODING HERE ###
    #######################


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='The script retrieves data from Pfam database (online or from cached file)'
                                                 ' and provides an output file'
                                                 ' with the strings "ProteinID   ProteinID   similarity", where'
                                                 ' similarity is a string with one of the values from '
                                                 ' different/ambiguous/similar.')

    parser.add_argument("-ids", "--protein_ids_file", help="File name of the Uniprot ids", required=True)
    parser.add_argument("-o", "--output_file", help="Output file name", required=True)

    ##########################
    ### START CODING HERE ####
    ##########################
    # If you would like to cache the results of pfam you would probably need to add a new parameter where the cache
    # file (files) is located.
    #######################
    ### END CODING HERE ###
    #######################

    args = parser.parse_args()

    protein_ids_file = args.protein_ids_file
    output_file = args.output_file

    main(protein_ids_file, output_file)