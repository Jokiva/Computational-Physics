import os

# file_paths = ['data/prob_3_' + str(index) + '.dat' for index in range(1, 4)]
script_paths = ['trapezoidal_err.py', 'simpson_err.py', 'romberg_err.py']

# let the user to decide if we will start a new run
# option = input('new run？\n Y/n:')
# if option == 'Y':
    # remove the previous data
#     for file in file_paths:
#         try:
#             os.system('rm -f ' + file)
#         except FileNotFoundError:
#             pass

    # run the scripts to generate the new data
#     for script in script_paths:
#         os.system('python ' + script)


# get the data
# line 0: number of intervals
# line 1: error
# line 2: a
# line 3: b
# for file in file_paths:
#     with open(file, 'rt') as f:
#         pass


for script in script_paths:
    os.system('python ' + script)

exit()
