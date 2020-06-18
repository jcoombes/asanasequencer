"""
I want to create a function which can take a pose as a string, then return a few seconds yoga video of the pose.
I imagine I will need to use ffmpeg for this?
"""
import os
import pprint
import csv
import sys

def find_pose_in_library(pose, directory):
    """
    pose :param str - which pose would you like to get?
    directory :param str - path to folder containing yoga subtitles.
    return location timestamps and video locations.
    """
    match_dict = {}
    pose = pose.lower()

    for dirpath, dirnames, filenames in os.walk(directory):
        # For now all the yoga videos and subtitle files are stored
        # loose in the same folder.
        subtitle_file_list = [i for i in filenames if i.endswith('.vtt')]
        video_file_list = [i for i in filenames if i.endswith(('.mkv', '.webm'))]
    subtitle_file_list.sort()
    video_file_list.sort()

    previous_line = ""

    for filename in subtitle_file_list:
        with open(os.path.join(directory, filename)) as f:
            for line in f:
                if "-->" in line:
                    most_recent_timestamp = line
                elif pose in line.lower():
                    key = filename[:3] + most_recent_timestamp[:-2]
                    # print(key, sep="")
                    # print(line, sep="")
                    match_dict[key] = line[:-2] #slice to remove the '\n'
    return match_dict

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=1)
    if len(sys.argv) == 1:
        pose == 'wiki'
    else:
        pose = sys.argv[1]

    if pose == 'wiki':
        #check the wikipedia list of asanas.
        with open('wikiadriene.txt', 'w+') as f:
            with open('wikipedialistofasanas.csv', 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                print(csv_reader.fieldnames)
                print("----------------------------")
                for row in csv_reader:
                    print(row["Asana"])
    else:
        match_dict = find_pose_in_library(pose,
                                          os.path.join("..", "yoga_library"))
        pp.pprint(match_dict)
        print(len(match_dict))