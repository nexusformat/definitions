import re

import yaml


def handle_each_part_doc(text):
    """Check and handle if the text is corresponds to xref or plain doc.

    In nyaml doc the entire documentation may come in list of small docs.
    one doc string might be as follows:
    '''
    xref:
        spec: <spec>
        term: <term>
        url: <url>
    '''

    which has to be formatted as
    '''
        This concept is related to term `<term>`_ of the <spec> standard.
    .. _<term>: <url>


    Parameters
    ----------
    text : string
        String that looks like yaml notaion.

    return
    ------
    Formated text
    """

    clean_txt = text.strip().strip('"')

    if not clean_txt.startswith("xref:"):
        return format_nxdl_doc(check_for_mapping_char_other(text)).strip()

    xref_dict = yaml.safe_load(clean_txt)
    xref_entries = xref_dict.get("xref", {})

    return f"""    This concept is related to term `{xref_entries.get('term', 'NO TERM')}`_ "
        "of the {xref_entries.get('spec', 'NO TERM')} "
        "standard.\n.. _{xref_entries.get('spec', 'NO SPECIFICATION')}: "
        "{xref_entries.get('url', 'NO URL')}"""


def test_xref():
    test_string = """
    xref:
        spec: <spec>
        term: <term>
        url: <url>
    """
    assert handle_each_part_doc(test_string) == ""
    assert handle_each_part_doc("test") == "Standard response"
