#!/usr/bin/env python

# Coded for both python2 and python3.

'''
Create release notes for a new relase of the GitHub repository.
'''

from datetime import datetime
import os, sys
import github
import collections
import argparse


CREDS_FILE_NAME = "__github_creds__.txt"        # put in ~/.config/ directory not readable by others
GITHUB_PER_PAGE = 30


def str2time(time_string):
    # Tue, 20 Dec 2016 17:35:40 GMT
    fmt = "%a, %d %b %Y %H:%M:%S %Z"
    return datetime.strptime(time_string, fmt)


def getCredentialsFile():
    search_paths = [
        os.path.dirname(__file__),
        os.path.join(os.environ["HOME"], ".config"),    # TODO: robust?
    ]
    for path in search_paths:
        full_name = os.path.join(path, CREDS_FILE_NAME)
        if os.path.exists(full_name):
            return full_name
    raise ValueError('Cannot find credentials file: ' + CREDS_FILE_NAME)


def findGitConfigFile():
    """
    return full path to .git/config file
    
    must be in current working directory or some parent directory
    
    This is a simplistic search that could be improved by using 
    an open source package.
    
    Needs testing for when things are wrong.
    """
    path = os.getcwd()
    for i in range(99):
        config_file = os.path.join(path, ".git", "config")
        if os.path.exists(config_file):
            return config_file
        # TODO: what if we reach the root of the file system?
        path = os.path.abspath(os.path.join(path, ".."))
    msg = "Could not find .git/config file in any parent directory."
    raise ValueError(msg)


def getRepositoryInfo():
    """
    return organization, repository from .git/config file
    
    This is a simplistic search that could be improved by using 
    an open source package.
    
    Needs testing for when things are wrong.
    """
    config_file = findGitConfigFile()
        
    # found it!
    found_origin = False
    with open(config_file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line == '[remote "origin"]':
                found_origin = True
            elif line.startswith("url"):
                url = line.split("=")[-1].strip()
                if url.find("github.com") < 0:
                    msg = "Not a GitHub repo: " + url
                    raise ValueError(msg)
                org, repo = url.rstrip(".git").split("/")[-2:]
                return org, repo


class ReleaseNotes(object):
    
    def __init__(self, base, head=None, milestone=None):
        self.base = base
        self.head = head or "master"
        self.milestone_title = milestone
        self.milestone = None

        self.commit_db = {}
        self.db = dict(tags={}, pulls={}, issues={}, commits={})
        self.organization, self.repository = getRepositoryInfo()
        self.creds_file_name = getCredentialsFile()
    
    def connect(self):
        uname, pwd = open(self.creds_file_name, 'r').read().split()
        self.gh = github.Github(uname, password=pwd, per_page=GITHUB_PER_PAGE)
        self.user = self.gh.get_user(self.organization)
        self.repo = self.user.get_repo(self.repository)
    
    def learn(self):
        base_commit = None
        earliest = None
        compare = self.repo.compare(self.base, self.head)
        commits = self.db["commits"] = collections.OrderedDict()
        for commit in compare.commits:
            commits[commit.sha] = commit
#         commits = self.db["commits"] = {commit.sha: commit for commit in compare.commits}
        
        for milestone in self.repo.get_milestones(state="all"):
            if milestone.title == self.milestone_title:
                self.milestone = milestone
                break
        if self.milestone is None:
            msg = "Could not find milestone: " + self.milestone
            raise ValueError(msg)

        tags = self.db["tags"]
        for tag in self.repo.get_tags():
            if tag.commit.sha in commits:
                tags[tag.name] = tag
            elif tag.name == self.base:
                base_commit = self.repo.get_commit(tag.commit.sha)
                earliest = str2time(base_commit.last_modified)

        pulls = self.db["pulls"]
        for pull in self.repo.get_pulls(state="closed"):
            if pull.closed_at > earliest:
                pulls[pull.number] = pull

        issues = self.db["issues"]
        for issue in self.repo.get_issues(milestone=self.milestone, state="closed"):
            if self.milestone is not None or issue.closed_at > earliest:
                if issue.number not in pulls:
                    issues[issue.number] = issue

    def print_report(self):
        print("## " + self.milestone_title)
        print("")
        if self.milestone is not None:
            print("**milestone**: [%s](%s)" % (self.milestone.title, self.milestone.url))
            print("")
        print("section | number")
        print("-"*5, " | ", "-"*5)
        print("New Tags | ", len(self.db["tags"]))
        print("Pull Requests | ", len(self.db["pulls"]))
        print("Issues | ", len(self.db["issues"]))
        print("Commits | ", len(self.db["commits"]))
        print("")
        print("### Tags")
        print("")
        for k, tag in sorted(self.db["tags"].items()):
            print("* [%s](%s) %s" % (tag.commit.sha[:7], tag.commit.html_url, k))
        print("")
        print("### Pull Requests")
        print("")
        for k, pull in sorted(self.db["pulls"].items()):
            state = {True: "merged", False: "closed"}[pull.merged]
            print("* [#%d](%s) (%s) %s" % (pull.number, pull.html_url, state, pull.title))
        print("")
        print("### Issues")
        print("")
        for k, issue in sorted(self.db["issues"].items()):
            if k not in self.db["pulls"]:
                print("* [#%d](%s) %s" % (issue.number, issue.html_url, issue.title))
        print("")
        print("### Commits")
        print("")
        for k, commit in self.db["commits"].items():
            message = commit.commit.message.splitlines()[0]
            print("* [%s](%s) %s" % (k[:7], commit.html_url, message))
        print("")


def main(base="v3.2", head="master", milestone="NXDL 3.3"):
    # github.enable_console_debug_logging()
    notes = ReleaseNotes(base, head=head, milestone=milestone)
    notes.connect()
    notes.learn()
    notes.print_report()


def parse_command_line():
    doc = __doc__.strip()
    parser = argparse.ArgumentParser(description=doc)

    help_text = "name of tag to start the range"
    parser.add_argument('base', action='store', help=help_text)

    help_text = "name of milestone"
    parser.add_argument('milestone', action='store', help=help_text)

    help_text = "name of tag, branch, SHA to end the range"
    help_text += ' (default="master")'
    parser.add_argument(
        "--head", 
        action='store', 
        dest='head',
        nargs='?', 
        help = help_text, 
        default="master")

    return parser.parse_args()


if __name__ == '__main__':
    cmd = parse_command_line()
    main(cmd.base, head=cmd.head, milestone=cmd.milestone)


# NeXus - Neutron and X-ray Common Data Format
# 
# Copyright (C) 2008-2018 NeXus International Advisory Committee (NIAC)
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For further information, see http://www.nexusformat.org
