#!/sbin/sh
java -classpath /usr/lib/classes.zip:../jnexus.jar:. \
	-Dneutron.nexus.JNEXUSLIB=../bin/du40/libjnexus.so TestJapi
