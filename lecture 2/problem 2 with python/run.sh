#!/bin/bash

# protect the original data
chmod -w raw.txt

# give permision to the python script
chmod +x preprocess.py
# run the python script
chmod +w data.txt
./preprocess.py
# protect the cleaned data
chmod -w data.txt

# now we can manipulate the cleaned data
# finding the smallest and largest velocity
#  save the smallest one to smallest_velo.txt
sort -n < data.txt | head -1 > smallest_velo.txt
#  save the largest one to largest_velo.txt
sort -n < data.txt | tail -1 > largest_velo.txt

# finding the brightest and faintest galaxy
# save the brightest one to brightest.txt
sort -n -k 4 < data.txt | head -1 > brightest.txt
# save the faintest one to faintest.txt
sort -n -k 4 < data.txt | tail -1 > faintest.txt

# make a new file galaxies.txt
touch galaxies.txt
paste -s smallest_velo.txt largest_velo.txt brightest.txt faintest.txt > galaxies.txt