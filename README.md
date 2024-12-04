# Cameras_Offline

Cameras_Offline is a Five Nights at Freddy's (FNAF) clone that uses audio clues instead of cameras. The goal of the game is to locate the monster by receiving audio cues from various sectors. After locating it, you must shock the monster to send it back to Sector 0. If the monster reaches Sector 12 (where you are), you lose.

The monster uses an algorithm to navigate the map. For example, if the monster is in Sector 3, it has a 40% chance of moving to Sector 2, a 10% chance of moving to Sector 1, a 30% chance of moving to Sector 5, a 30% chance of moving to Sector 7, and a 20% chance of moving to Sector 6.

The monster also utilizes 3D audio, allowing you to hear its position from the right, left, front, and behind. One issue I encountered with 3D audio was that I couldn’t figure out how to make WAV files play exclusively in one ear of the headphones. To solve this, I created different WAV files for each sound location using Adobe Audition.

Another challenge I faced was menu navigation. Initially, I wanted the player to click on options, similar to FNAF, but this proved too complex and caused several issues. I also tried using arrow keys for menu navigation, but that created speed-related problems. I ultimately decided to use typing-based navigation, as it was easier to implement and aligned well with most of the labs, which were already type-based.

One more issue was that the monster wasn’t attacking independently; it would wait for you to select an option before moving or attacking. I discovered that running the monster logic on a separate screen helped resolve this issue.

I consider this version of the game a demo because I genuinely want to continue working on this project during winter break. I hope you’ll enjoy it!