#!/usr/bin/tcsh

########### SVN repository information ###################
# $Date: 2008$
# $Author$
# $Revision$
# $HeadURL$
# $Id$
########### SVN repository information ###################

# purpose: sets date/time/svnid as subtitle of manual

set svnid = `svnversion ..`

echo '<?xml version="1.0" encoding="UTF-8"?>'
echo '<?oxygen '
echo '    RNGSchema="http://www.oasis-open.org/docbook/xml/5.0/rng/docbookxi.rng" '
echo '    type="xml"?>'
echo '<subtitle '
echo '    xmlns="http://docbook.org/ns/docbook" '
echo '    version="5.0">'
echo '    <\!-- manual was last rebuilt on this date/time -->'
echo '    Id:' ${svnid}, `date`
echo '</subtitle>'
