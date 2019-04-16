#!/bin/bash

#Paul Bosonetto


for file in "$1"* 
do
	mv "$file"  "${file/ /_}"
done
