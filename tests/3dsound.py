from openal import *
import time

# Initialize OpenAL
oalInit()

# Set the distance model globally (this should be done once at the beginning)
alDistanceModel(AL_LINEAR_DISTANCE)  # Set distance model to linear attenuation

# Create a listener and set position and orientation
listener = oalGetListener()
listener.set_position((40, 0, 0))  # Position the listener at (20, 0, 0)
listener.set_orientation((0, 0, -1, 0, 1, 0))  # Listener facing along negative Z-axis

# Create a source and load the sound
source = oalOpen("door.wav")
source.set_position((0, 0, 0))  # Position the source at the origin (0, 0, 0)
source.set_velocity((0, 0, 0))  # Static source (no movement)

# Set the reference and max distance for the source (attenuation settings)
source.set_reference_distance(1.0)  # Distance at which the sound is full volume
source.set_max_distance(30.0)  # Max distance at which the sound is still audible

# Play the source
source.play()

# Wait for the playback to finish
while source.get_state() == AL_PLAYING:
    time.sleep(1)

# Cleanup
oalQuit()

