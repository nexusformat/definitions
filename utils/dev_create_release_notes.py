#!/usr/bin/env python

'''
Developers: use this code to develop and test create_release_notes.py
'''
import os

CREDS_FILE = os.path.join(
    os.environ["HOME"],
    ".config",
    "github_token",
)

with open(CREDS_FILE, "r") as cf:
    token = cf.read().strip()

from create_release_notes import main
main(
    base="v2018.5", 
    head="main", 
    milestone="NXDL 2020.1", 
    token=token,
    debug=True)
