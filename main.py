import os
import random

folder = "I:\\" # Where the video files to be shuffled and renamed are stored, i used a usb drive, but change accordingly
files = [f for f in os.listdir(folder) if f.endswith(('.mp4', '.mkv', '.avi'))] # Sorts thru ALL file types to find video files
numbers_list = [] # List of all possible prefixes
for i in range(len(files)): 
    numbers_list.append(f"{i+1}.") # creates a list of prefixes that will always match the amount of appropriate video files

# print("1", files)

# Prefix remover
for filename in files: # filters thru all video file names in files list
    for number in numbers_list: # filters thru all prefixes of numbers_list
        if number in filename: # compares one by one the prefixes with the video file names and selects it if there is a match
            clean_name = filename[3:] # removes the prefix, which is always the first 3 characters
            os.rename(os.path.join(folder, filename), os.path.join(folder, clean_name)) # changes file names BUT NOT THE files list!!!
            # print("2", files, number)
            index = numbers_list.index(number) # finds index of relevant prefix
            files[index] = clean_name # replaces old prefix file name with the corresponding new non-prefix file name in the files list
            # print("3", files)

random.shuffle(files)
# print("4", files)

for idx, file in enumerate(files): # assigns a number counting up to each file in  the files list
    new_name = f"{idx+1}. {file}" # creates a new name by combining the index from the enumerate (+1 as index start at 0) with the file name
    os.rename(os.path.join(folder, file), os.path.join(folder, new_name)) # changes the file names
    # print("5", files)

# print("6", files)
