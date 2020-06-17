"""
I want to create a function which can take a pose as a string, then return a few seconds yoga video of the pose.
I imagine I will need to use ffmpeg for this?
"""
import os

def find_pose_in_library(pose, directory):
    """
    pose :param str - which pose would you like to get?
    directory :param str - path to folder containing yoga subtitles.
    return location timestamps and video locations.
    """
    for dirpath, dirnames, filenames in os.walk():
        print ()