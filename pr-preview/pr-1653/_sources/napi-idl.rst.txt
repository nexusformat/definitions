.. index:: NAPI; IDL

.. _NAPI-Core-idl:

==========================================
NAPI IDL Interface
==========================================

IDL is an interactive data evaluation environment developed by Research Systems - it is an interpreted language
for data manipulation and visualization. The NeXus IDL bindings allow access to the NeXus API from within
IDL - they are installed when NeXus is compiled from source after being configured with the following options::

	configure \
		--with-idlroot=/path/to/idl/installation \
		--with-idldlm=/path/to/install/dlm/files/to

For further details see the README 
(https://htmlpreview.github.com/?https://github.com/nexusformat/code/blob/master/bindings/idl/README.html) 
for the NeXus IDL binding. The source code is stored at https://github.com/nexusformat/code/tree/master/bindings/idl
