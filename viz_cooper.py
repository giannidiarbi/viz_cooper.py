#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:38:56 2023

@author: giannidiarbi
 DS2000
 Spring 2023
 HW 2 Problem 3
 viz_cooper.py
 
 Test case:
     Distance = 2.8284 units
     Feet = 2,262.72
     Miles = 0.4285
     I want to cover 0.4285 miles in 10 minutes
     = 2.571 miles per hour
"""

import matplotlib.pyplot as plt

DISTANCE_FILE = "distances_to_cooper.txt"
FEET_CONVERTER = 800
MILES_CONVERTER = 5280

def main():
    # Gather data - read in the data for 3 people's distances from Cooper
    with open(DISTANCE_FILE, "r") as infile: 
        distance1 = float(infile.readline().strip())
        distance2 = float(infile.readline().strip())
        distance3 = float(infile.readline().strip())
    
    # Computation - convert each distance into feet
    feet1 = distance1 * FEET_CONVERTER
    feet2 = distance2 * FEET_CONVERTER
    feet3 = distance3 * FEET_CONVERTER
        
    # Convert each distance from feet to miles
    miles1 = feet1  / MILES_CONVERTER
    miles2 = feet2 / MILES_CONVERTER
    miles3 = feet3 / MILES_CONVERTER
    
    # Determine each person's walking speed (MPH) that will allow them to
    # reach Cooper in 10 minutes.
    speed1 = miles1 * 6
    speed2 = miles2 * 6
    speed3 = miles3 * 6
        
    # Communication - plot distance (ft) vs MPH
    plt.plot(feet1, speed1, "o", color = "magenta")
    plt.plot(feet2, speed2, "o", color = "darkgreen")
    plt.plot(feet3, speed3, "o", color = "darkorange")
    
    # Change the ranges for x and y axes
    plt.xlim(1000, 2400)
    plt.ylim(1.1, 2.8)
    
    # Add labels to axes, and title
    plt.xlabel("Distance (ft)")
    plt.ylabel("Walking Speed (MPH)")
    plt.title("Distance (ft) vs Required Walking Speeds (MPH)")
    
main()