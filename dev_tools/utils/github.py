import os

import requests


def format_author_name(nm):
    """
    make sure all words in name start with a capital
    """
    nms = nm.split(" ")
    auth_nm = " ".join([n.capitalize() for n in nms])
    return auth_nm


def get_github_profile_name(email):
    """
    given an email addr return the github login name
    """
    email = email.replace(" ", "")
    nm = email.split("@")[0]
    return nm


def get_file_contributors_via_api(repo_name, file_path):
    """
    This function takes the repo name (ex:"definitions") and relative path to the nxdl
    file (ex: "applications/NXmx.nxdl.xml") and using the github api it retrieves a dictionary
    of committers for that file in descending date order.

    In order to increase the capacity (rate) of use of the github API an access token is used if it exists
    as an environment variable called GH_TOKEN, in the ci yaml file this is expected to be assigned from the secret
    object like this
    env:
          GH_TOKEN: ${{ secrets.GH_TOKEN }}

    With the access token the rate is 5000 times per hour and without it is 60

    returns a sorted dict of unique contributors to a file, or None if no GH_TOKEN has been defined in os.environ
    """
    have_token = False
    access_token = os.getenv("GH_TOKEN")
    if (
        access_token is not None and access_token != "NONE"
    ):  # latter clause is false in most CI cases
        if len(access_token) > 0:
            have_token = True
    else:
        # because the environment does not contain GH_TOKEN, assume the user wants to build the
        # docs without contributor info
        return None

    contrib_skip_list = ["GitHub"]
    url = f"https://api.github.com/repos/nexusformat/{repo_name}/commits"
    params = {"path": file_path}
    headers = {}
    if have_token:
        # Set the headers with the access token
        headers = {
            "Authorization": f"token {access_token}",
            "Accept": "application/vnd.github.v3+json",
        }

    response = requests.get(url, params=params, headers=headers)
    commits = response.json()
    if response.status_code != 200:
        # if its 403: the max rate per hour has been reached
        raise Exception(
            f"access_token={access_token}, {commits['message']},{commits['documentation_url']}"
        )

    contributor_names = set()
    contribs_dct = {}
    _email_lst = []
    for commit_dct in commits:
        if commit_dct["committer"] is not None:
            contributor = commit_dct["commit"]["committer"]["name"]
            if contributor in contrib_skip_list:
                continue
            contributor_names.add(contributor)
            if commit_dct["commit"]["committer"]["email"] not in _email_lst:
                _email = commit_dct["commit"]["committer"]["email"]
                _email_lst.append(_email)
                contribs_dct[commit_dct["commit"]["committer"]["date"]] = {
                    "name": format_author_name(
                        commit_dct["commit"]["committer"]["name"]
                    ),
                    "commit_dct": commit_dct,
                }

    # sort them so they are in descending order from newest to oldest
    sorted_keys = sorted(contribs_dct.keys(), reverse=True)
    sorted_dict = {key: contribs_dct[key] for key in sorted_keys}

    return sorted_dict
