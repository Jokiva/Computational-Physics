 # remove the comments and save data to data0.txt
 sed 's/#/#\n/g' < lcrs.txt | sed '1,4d' > data0.txt
 # replace ' ' by '\n' and extract the numerical data
 sed 's/ /\n/g' < data0.txt | grep '[0-9]' > data1.txt
 # reshape the data into four columns
 awk 'ORS=NR%4?" ":"\n"{print}' < data1.txt > data.txt


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