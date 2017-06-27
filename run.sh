#!/bin/bash

mkdir -p results

for file in $(ls input/* | sed 's/input\///;s/.txt$//'); do
    FOLDER="results/$file"
    rm -rf $FOLDER
    for i in 1 2 3; do
        mkdir -p $FOLDER/$i
        pushd "${FOLDER}/${i}"
            ../../../cut2d.py < ../../../input/"${file}.txt"
        popd
    done
done
