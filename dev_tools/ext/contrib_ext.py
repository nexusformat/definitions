import re

# a custom sphinx extension that is connected to the source-read hook for rst files,
# the purpose is to read all of the contributor information from the rst file and
# place it in a string variable that will be used in the sourcelink.html jinja template
# that has been over ridden and sits in the _templates directory to produce the
# contributor information on the for right sidebar of the html pages

variables_re = re.compile(r"\|(\w+)\| replace::\s(.+)")


def extract_contributor_vars(app, docname, source):
    # Read the RST file content
    content = source[0]

    # Extract variables using regular expressions
    variables = variables_re.findall(content)

    # Create a dictionary to store the extracted variables
    # this will create a list of single strings each of which contain the info about the contributor
    extracted_variables = [var[1] for var in variables]
    if "variables" not in app.config.html_context.keys():
        app.config.html_context["variables"] = {}

    # Add the extracted variables to the Jinja environment
    app.config.html_context["variables"][docname] = extracted_variables


def setup(app):
    app.connect("source-read", extract_contributor_vars)
