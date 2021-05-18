"""
File: video.py
Author: Alexander Lee (https://github.com/alex36540)

Description: Contains representation of a video as well as operations on a playlist pertaining
             to videos.
"""
from dataclasses import dataclass

VID_URL = "https://www.youtube.com/watch?v="

@dataclass(unsafe_hash=True)
class Video:
    """Class that represents a video"""
    id: str
    title: str
    index: int
