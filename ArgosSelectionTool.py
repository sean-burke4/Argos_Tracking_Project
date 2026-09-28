#-------------------------------------------------------------
# ArgosSelectionTool.py
#
# Description: Reads in an Argos tracking data file and allows
#   the user to identify the tracked sitings found within a 
#   specified bounding box.
#
# Author: Sean Burke (sb924@duke.edu)
# Date:   Fall 2026
#--------------------------------------------------------------

# Create the geographic selection box
the_box = {
    'x_min' : 34.00,
    'y_min' : -76.00,
    'x_max' : 34.50,
    'y_max' : -75.00
}

# Copy and paste a line of data as the lineString variable value
lineString = ''
    
# Use the split command to parse the items in lineString into a list object
line_data = lineString
  
# Assign variables to specfic items in the list
event_id = line_data[]   # Argos tracking event ID ("event-id")
timestamp = line_data[]  # Observation date ("timestamp")
lat = line_data[]        # Observation latitude  ("location-lat")
lon = line_data[]        # Observation longitude ("location-lon")
lc  = line_data[]        # Observation location class ("argos:lc")
tag_id = line_data[]     # Tag identifier ("tag-local-identifier")
  
# Print information to the use
print (f"Record {event_id} indicates {tag_id} was seen at {lat}N and {lon}W on {timestamp}")