from class_code import meet_code
import pyautogui as pt
import time
import datetime
import calendar
import json

MEET_ICON_POS = (29, 517)  # (x, y)
TEXT_BOX = (1103, 469)  # The box where the code for the meeting has to typed
MUTE_MIC_ICON_POS = (463, 672)
CAMERA_OFF_ICON_POS = (542, 677)
JOIN_BUTTON = (1072, 509)
AVERAGE_DELAY = 5

time_table = json.load(open("time_table.json"))
week_name = calendar.day_name[datetime.date.today().weekday()].lower()
today_date = datetime.date.today().strftime("%d-%m-%y")


t_time_table = time_table[week_name]  # todays time table
curr_time = datetime.datetime.now()

with open("session.txt", "r") as file:
    session = int(file.readline(1))


def update_session(value):
    with open("session.txt", "w") as f:
        f.write(str(value))


def is_time_for_session(join_time, join_before):

    if curr_time >= join_time and join_before > curr_time:
        return True

    else:
        return False


def join_class(subject: str):
    """
    This function does not use the browser to open google meet instead it uses the shortcut icon made 
    for the google meet website with the designated email address. 
    """

    # Click the shortcut icon
    pt.click(MEET_ICON_POS[0], MEET_ICON_POS[1])
    time.sleep(AVERAGE_DELAY)
    # Click enter a meeting code option
    pt.click(TEXT_BOX[0], TEXT_BOX[1])
    # Enter the code
    pt.write(meet_code[subject])
    # Press enter
    pt.press("enter")
    time.sleep(AVERAGE_DELAY + 2)
    # Click mute mic and hide camera option
    pt.click(MUTE_MIC_ICON_POS[0], MUTE_MIC_ICON_POS[1])
    pt.click(CAMERA_OFF_ICON_POS[0], CAMERA_OFF_ICON_POS[1])
    # Click join
    pt.click(JOIN_BUTTON[0], JOIN_BUTTON[1])
    # print("Did you join the session ? \n If yes type 'y' else press enter...")
    ans = input("Did you join the session ? \n If yes type 'y' else press enter...")
    if ans.lower() == "y":
        if str(session + 1) in t_time_table:
            update_session(2)

        else:
            update_session(1)


def on_start():
    session_join_before = datetime.datetime.strptime(
        today_date + " " + t_time_table[str(session) + "-join-before"], "%d-%m-%y %H:%M"
    )

    join_time = datetime.datetime.strptime(
        today_date + " " + t_time_table[str(session)], "%d-%m-%y %H:%M"
    )

    if is_time_for_session(join_time, session_join_before):
        join_class(t_time_table[str(session) + "-subject"])


# test_time = "8:30"
# join_before = "9:30"
# _new = today_date + " " + test_time
# _new = datetime.datetime.strptime(_new, "%d-%m-%y %H:%M")
# _new_join = today_date + " " + join_before
# _new_join = datetime.datetime.strptime(_new_join, "%d-%m-%y %H:%M")
# print(is_time_for_session(_new, _new_join))


if __name__ == "__main__":
    on_start()
