#!/bin/bash


#Starting line of a bash script

set -e
for file in *; do
    if [[ $file == *.yaml ]]; then
        echo "Converting $file to NXDL"
        nyaml2nxdl $file
    fi
done


for file in *; do
    if [[ $file == *.nxdl.xml ]]; then
        echo "Converting $file to NYAML"
        nyaml2nxdl $file
        mv $file ../../
    fi
done

for file in *; do
    if [[ $file == *_parsed.yaml ]]; then
        mv $file $(echo $file | sed 's/_parsed//')
    fi
done

for file in *; do
    if [[ $file == *.yaml ]]; then
        cp $file ../
    fi
done

rm ../../NXbias_spectroscopy_old.nxdl.xml
rm ../../NXspm_v1_backup.nxdl.xml
rm ../NXbias_spectroscopy_old.yaml
rm ../NXspm_v1_backup.yaml

