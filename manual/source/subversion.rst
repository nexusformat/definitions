.. $Id$

.. _Subversion:

=============================
NeXus Subversion Repositories
=============================

NeXus NXDL class definitions (both base classes and instruments) and
the NeXus code library source are held in a pair of *subversion* [#]_ repositories.
The repositories are world readable. You can browse them directly:

:NeXus code library and applications:
	http://svn.nexusformat.org/code

:NeXus NXDL class definitions
	http://svn.nexusformat.org/definitions

Better looking interfaces are also provided using 
*ViewVC* [#]_ and *TRAC* [#]_.  These software tools 
have been added to the NeXus WWW site server.

.. [#] **ViewVC**: http://www.viewvc.org 
.. [#] **TRAC**: http://trac.edgewall.org

Browse the NeXus version control repositories:

+ *code* repository (NAPI, library, and applications)

  - **ViewVC** http://svn.nexusformat.org/viewvc/NeXusCode
  - **TRAC**   http://trac.nexusformat.org/code/browser

+ *definitions* repository (NXDL classes and manual source)

  - **ViewVC** http://svn.nexusformat.org/viewvc/NeXusDefinitions
  - **TRAC**   http://trac.nexusformat.org/definitions/browser

The repository can also be interrogated for recent updates via a
*query form*, such as:

.. code-block:: guess

    http://svn.nexusformat.org/viewvc/NeXusCode/trunk/?view=queryform

For example, show me all changes in the last month for the
code (library and applications) repository:

.. code-block:: guess

    http://svn.nexusformat.org/viewvc/NeXusCode/trunk/?view=query&date=month&limit_changes=100

or the from the **Definition repository**:

.. code-block:: guess

    http://trac.nexusformat.org/definitions/timeline?daysback=30

If you wish to receive an email when a change is made to the repository you
should join the appropriate :ref:`Mailing Lists <MailingLists>`.

+-------------------------------------------------------------------+---------------------------+
|*XML RSS Feed*                                                     | icon                      |
+===================================================================+===========================+
|Alternatively, you can use an RSS feed to keep abreast of changes. | .. image:: img/rssfeed.jpg|
|TRAC provides a link to its RSS feed on pages with an orange       |     :scale: 50%           |
|*XML RSS Feed* icon at their foot such as:                         |                           |
+-------------------------------------------------------------------+---------------------------+


There are pages that show the subversion repository activity in a timeline
format or a tabular (revision log) format.

:code (library and applications) repository timeline:
    http://trac.nexusformat.org/code/timeline

:definitions repository timeline:
    http://trac.nexusformat.org/definitions/timeline

:code repository revision log:
    http://trac.nexusformat.org/code/log

:definitions repository revision log:
    http://trac.nexusformat.org/definitions/log

.. _Subversion-Login:

Login
#####

To update files in these repositories you will need to use
a subversion client such as *TortoiseSVN* (http://tortoisesvn.tigris.org)
for Microsoft Windows or ``svn`` for command-line shells
and also provide your NeXus Wiki username and password.
Note that for subversion write access:

- If your Wiki username contains a space, write it with a
  space (i.e. do not replace the space with an _ as is
  done in WIKI URLs)

- You cannot use a *temporary password*
  (i.e. one that was
  emailed to you in response to a request). You must first
  log into MediaWiki with the temporary password and then
  go to your account section
  (http://www.nexusformat.org/Special:Preferences)
  and change the password.

- Your Wiki account must have an email address associated
  with it and this address must have been validated.
  To provide and/or validate your email address,
  log in and go to your account section
  (http://www.nexusformat.org/Special:Preferences).

- If you have login problems and have not changed your
  WIKI password since 20th October 2006, please go to the
  NeXus wiki login page (http://www.nexusformat.org/Special:UserLogin)
  and request a new password to be sent by email.
  To synchronise TRAC/Subversion/MediaWiki
  required some changes to the authentication system which
  will have invalidated passwords set prior to that date.

Here are the URLs to access the subversion repositories as a developer:

:code for library/applications:
    https://svn.nexusformat.org/code/trunk

:definitions for NXDL classes:
    https://svn.nexusformat.org/definitions/trunk

:checkout the code trunk:
    .. code-block:: guess

        svn co --username "use your WIKI Username" https://svn.nexusformat.org/code/trunk nexus_code

Please report any problems via the
:ref:`Issue Reporting <IssueReporting>`
system.

.. _Subversion-CommittingChanges:

Committing Changes
##################

As well as needing a valid account, you will not be able to
check-in changes unless you indicate (in the log message
attached to the commit) which current issues on the
:ref:`Issue Reporting <IssueReporting>`
system the changes either fix or refer to.
This is done by enclosing special phrases in the commit
message of the form:

.. literalinclude:: examples/ex-svn-commit-message-syntax.txt
    :tab-width: 4
    :linenos:
    :language: guess

where ``command`` is one of the commands detailed
below and ``#1`` means *issue number
1* on the system, etc.
You can have more then one command in a message. The following
commands are supported and there is more then one spelling for
each command (to make this as user-friendly as possible):

``closes, fixes``
    The specified issue numbers are closed with the
    contents of this commit message being added to it.

``references, refs, addresses, re``
    The specified issue numbers are left in their
    current status, but the contents of this commit
    message are added to their notes.

For example, the commit message

.. code-block:: guess

    Changed blah and foo to do this or that. Fixes #10 and #12, and refs #12.

This will close issues #10 and #12, and add a note to #12 on the
:ref:`Issue Reporting <IssueReporting>`
system. For a list of current issues, see:

+ Active tickets for the NeXus code library:
	http://trac.nexusformat.org/code/report/1

+ Active tickets for NeXus definitions:
	http://trac.nexusformat.org/definitions/report/1

.. _Subversion-URLs:

URLs described in this section
##############################

Many Uniform Resource Locators (URLs) have been used in this section.
This is a table describing them.

Subversion revision management software
    http://subversion.apache.org/

ViewVC versions control repository viewing software
    http://www.viewvc.org/

TRAC issue management software
    http://trac.edgewall.org

TortoiseSVN, Windows subversion client
    http://tortoisesvn.tigris.org/

NeXus code (library and applications) subversion repository
    http://svn.nexusformat.org/code/

NeXus definitions subversion repository
    http://svn.nexusformat.org/definitions/

ViewVC view of NeXus code (library and applications) repository
    http://svn.nexusformat.org/viewvc/NeXusCode

ViewVC view of NeXus definitions repository
    http://svn.nexusformat.org/viewvc/NeXusDefinitions

TRAC view of NeXus code (library and applications) repository
    http://trac.nexusformat.org/code/browser

NeXus code (library and applications) revision log
    http://trac.nexusformat.org/code/log

Active tickets for the NeXus code repository
    http://trac.nexusformat.org/code/report/1

NeXus code repository timeline
    http://trac.nexusformat.org/code/timeline

TRAC view of NeXus definitions repository
    http://trac.nexusformat.org/definitions/browser

NeXus definitions revision log
    http://trac.nexusformat.org/definitions/log

Active tickets for NeXus definitions
    http://trac.nexusformat.org/definitions/report/1

NeXus definitions repository timeline
    http://trac.nexusformat.org/definitions/timeline

NeXus code repository (password required)
    https://svn.nexusformat.org/code/trunk

NeXus definitions repository (password required)
    https://svn.nexusformat.org/definitions/trunk


.. [#] *subversion*, revision control software: http://subversion.apache.org
