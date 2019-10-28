import os
# Walking a directory tree and printing the names of the directories and files
counterFiles = 0
counterDir = 0
for dirpath, dirnames, files in os.walk('/home/maluki/Documents'):
    print(f'Found directory: {dirpath}')
    counterDir = counterDir + 1
    for file_name in files:
    	counterFiles = counterFiles + 1
    	print(file_name)

print('The number of files in the directory is {} and number of directories is {}'.format(counterFiles, counterDir))
