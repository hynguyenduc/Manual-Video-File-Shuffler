## Manual-Video-File-Shuffler
Python script that shuffles and renames video files in a folder using .bat and .vbs files

# Purpose
This is more of a Python refresher for me and how to run those scripts without needing to access the terminal and typing 'python3 main.py'

# How it works
There are more in-depth notes in the main.py file, but I will list a brief rundown here.

- Script will start sorting through all the files for relevant video files (mp4, avi, mkv)
- It will create a list that matches the amount of relevant video files to create prefixes to attach to the video files later
- Next it will remove any lingering prefixes from the previous shuffle and renaming by identifying if the prefixes in the list created earlier are in the names of the video files
- Then the shuffling happens
- Lastly, the newly shuffled video files are renamed by adding a numbered prefix to their file names
- The vbs file will run the code via the bat file without visibly launching the terminal

  
