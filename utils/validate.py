#!/usr/bin/env python
NXCONVERT = "nxconvert"

def getSourceDir():
  """Returns the location of the source code."""
  import os
  import sys
  script = os.path.abspath(sys.argv[0])
  if os.path.islink(script):
    script = os.path.realpath(script)
  return os.path.dirname(script)

def run(cmd, **kwargs):
  """Execute the supplied command and return the tuple (return value,
  stdout)"""
  shell = kwargs.get("shell", True)

  import subprocess as sub
  proc = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.STDOUT, shell=shell)
  (stdout, stderr) = proc.communicate()
  return_code = proc.wait()
  return (return_code, stdout)

def nxconvert(definition=None, input=None, output=None, verbose=0):
  if definition is None:
    command = "%s -d %s %s" % (NXCONVERT, input, output)
  else:
    command = "%s -D%s %s %s" % (NXCONVERT, definition, input, output)
  (code, stdout) = run(command)
  if verbose > 1 or code != 0:
    print command
    print stdout
  if code != 0:
    raise RuntimeError(NXCONVERT + " returned " + str(code))

def process(xml=None, xslt=None, output=None, verbose=0):
  if xml is None:
    raise Exception("xml file is None")
  if xslt is None:
    raise Exception("xslt file is None")
  XSLTPROC = "java -jar %s/saxon9he.jar" % (getSourceDir())
  if output is None :
    command = "%s %s %s" % (XSLTPROC, xml, xslt)
  else:
    command = "%s %s %s > %s" % (XSLTPROC, xml, xslt, output)
  print command
  (code, stdout) = run(command)
  if output is None :
    print stdout
  if verbose > 1 or code != 0:
    print command
    print stdout
  if code != 0:
    raise RuntimeError(XSLTPROC + " returned " + str(code))

def schematron2xslt(schematron=None, xslt=None, verbose=0):

  source_dir = getSourceDir()
  import os
  xslt1 = os.path.join(source_dir, "iso_dsdl_include.xsl")
  xslt2 = os.path.join(source_dir, "iso_abstract_expand.xsl")
  xslt3 = os.path.join(source_dir, "iso_svrl_for_xslt2.xsl")

  xslt_skel = os.path.join(source_dir, "iso_schematron_skeleton_for_saxon.xsl")

  (path, name) = os.path.split(schematron)
  schematron1 = name + ".step1"
  schematron2 = name + ".step2"

  #process(schematron, xslt1, schematron1, verbose)
  #process(schematron1, xslt2, schematron2, verbose)
  #os.remove(schematron1)
  #process(schematron2, xslt3, xslt, verbose)
  #os.remove(schematron2)
  process(schematron, xslt_skel, xslt, verbose)
  
  "xslt -stylesheet theSchema.xsl  myDocument.xml > myResult.xml"

if __name__ == "__main__":
  import os
  import sys

  VERBOSE = 1

  if len(sys.argv) < 2 :
    raise RuntimeError("Must give arg 1 (schemtron file)")
  schematron = sys.argv[1]

  if len(sys.argv) < 3 :
    raise RuntimeError("Must give arg 2 (input file)")
  in_file = sys.argv[2]

  if len(sys.argv) < 4 :
    out_file = None
  else:
    out_file = sys.argv[3]

  temp_xsl = "schema.xslt"

  xml_file = "reducednexus.xml"
  #nxconvert(None, in_file, xml_file, VERBOSE)
  xml_file = in_file

  schematron2xslt(schematron, temp_xsl, VERBOSE)
  process(xml_file, temp_xsl, out_file, VERBOSE)
  os.remove(temp_xsl)
