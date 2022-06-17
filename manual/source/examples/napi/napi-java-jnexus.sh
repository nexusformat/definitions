#!/sbin/sh
java -classpath /usr/lib/classes.zip:../jnexus.jar:. \
	-Dorg.nexusformat.JNEXUSLIB=../libjnexus.so TestJapi
