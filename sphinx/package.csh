#!/bin/csh

# $Id$

make html latexpdf
cd build
cp latex/nexus.pdf html/
tar czf ../html.tar.gz html
cd ..
