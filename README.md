# online_class_automation
Allows me to join my online classes accordingly


### Usage

To use this project, download the git repo and open the terminal and run.

```bash
pip3 install ptautogui
```
after the installation make a file named class_code.py which has a dict named meet_code.

```python
meet_code = {
    "physics": "********",
    "maths": "********",
    "chemistry": "********",
    "ip": "********",
    "english": "********",
    "test": "********",
}
```

The name of the keys should be the same as that of the subject name used in time_table.json file.
The current time table is set to my time table.
While modifying it make sure to use the naming convention as it is.

```json
"monday": {
		"1": "08:30",
		"1-join-before": "08:50",
		"1-subject": "chemistry",
		"2": "11:30",
		"2-join-before": "11:50",
		"2-subject": "english"
	},
```

Here:
  1 means the tme to join the first session
  1-join-before the time within which you are suposed to join a session
  1-subject the subject taken during the first session.
  
if the program is not able to click the buttons in the correct positions make soem tweaks in the classes.py.
There at the top the file some constants have been set.

```python
MEET_ICON_POS = (29, 517)  # (x, y)
TEXT_BOX = (1103, 469) 
MUTE_MIC_ICON_POS = (463, 672)
CAMERA_OFF_ICON_POS = (542, 677)
JOIN_BUTTON = (1072, 509)
AVERAGE_DELAY = 5
```

Here:
  MEET_ICON_POS is the position of the icon on the screen.
  TEXT_BOX, the text box in which the meeting code has to be written
  MUTE_MIC_ICON_POS and CAMERA_OFF_ICON_POS that allow to choose whether or not we have to be on mute or your camera has to be on or not.
              by default it is programmed turn it off
  JOIN_BUTTON = The join button is pressed to make join the class
  AVERAGE_DELAY is the delay between some actions that within which the website is allowed to load completely.
