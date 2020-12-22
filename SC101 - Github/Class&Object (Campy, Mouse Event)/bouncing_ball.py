"""
File: bouncing_ball.py
Name: Ethan Huang
-------------------------
TODO:
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.


** EXTENSION **
I built several signs to guide the users:

1. when the ball is at the initial position and the window is clickable
    -> build_a_sign() -- 'Click Anywhere'
2. when the ball is bouncing so the window is not clickable
    -> build_stop_sign() -- 'Stop Clicking'
3. when the ball is at the initial position and the window is clickable
    -> build_special_stop_sign() -- 'Stop Clicking' (with random color)

"""


from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
import random


VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

count = 3  # The users have three chances to click the ball
can_click = True  # A button to determine whether the mouse is clickable


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball = build_a_ball()
    window.add(ball)
    sign = build_start_sign()
    window.add(sign)
    onmouseclicked(start)


def start(mouse):
    """
    This function will first use can_click to control whether the program is clickable,
    and then use count to keep track on the times the users have played (users can only play three times).

    Once the ball starts to move, can_click will be assigned False, and the users are not allow to click,
    meanwhile, the stop_sign will appear to notice the users.

    Once the ball exits the window, it will return to the initial position,
    the window is clickable again, and the start_sign will appear to notice the users.

    When count < 0, the users can no longer make the ball move.
    the background will turn grey, and the special_stop_sign will appear to notice the users.

    """
    global count, can_click
    if can_click:
        # The ball is at the start position
        # Users can click to make the ball move, the mouse is clickable
        can_click = False  # Turn off the clickable function
        window.clear()
        ball = build_a_ball()
        window.add(ball)
        vy = GRAVITY
        while True:
            # The ball is moving
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y + SIZE >= window.height:
                # Hits the ground
                vy *= -REDUCE
            pause(DELAY)

            if ball.x + SIZE >= window.width:
                # Restart
                window.clear()
                count -= 1
                if count > 0:
                    sign = build_start_sign()
                    window.add(sign)
                    can_click = True
                else:
                    window.add(build_background())
                window.add(build_a_ball())
                break  # Return to the fist position again

    else:
        if count > 0:
            # Users are not able to click because the ball is bouncing
            window.add(build_stop_sign())
        else:
            # Users have already played for three times, so the clicks will no longer work
            window.add(build_background())
            window.add(build_a_ball())
            window.add(build_special_stop_sign())


def build_a_ball():
    """
    This function creates a ball with GOval
    :return: object, ball
    """
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    ball.fill_color = 'lightpink'
    ball.color = 'lightpink'
    return ball


def build_start_sign():
    """
    This function creates a start sign with GLabel
    :return: object, sign
    """
    sign = GLabel('Click Anywhere !!!', x=START_X+40, y=START_Y+10)
    sign.color = 'dimgrey'
    sign.font = 'Times New Roman-15-italic-bold'
    return sign


def build_stop_sign():
    """
    This function creates a stop sign with GLabel
    :return: object, sign
    """
    random_x = random.randint(0, 640)
    random_y = random.randint(30, 500)
    sign = GLabel('Stop Clicking !!! ', x=random_x, y=random_y)
    sign.color = 'firebrick'
    sign.font = 'Times New Roman-15-bold'
    return sign


def build_special_stop_sign():
    """
    This function creates a special stop sign with GLabel
    :return: object, sign
    """
    random_x = random.randint(0, 600)
    random_y = random.randint(30, 500)
    sign = GLabel(random_word(), x=random_x, y=random_y)
    sign.color = random_color()
    sign.font = 'Times New Roman-20-bold'
    return sign


def random_word():
    """
    This function chooses a random sign for the special stop sign.
    :return str, a sign for the special stop sign
    """
    num = random.choice(range(5))
    if num == 0:
        return "Stop Clicking"
    elif num == 1:
        return "Stop Clicking"
    elif num == 2:
        return "Stop It"
    elif num == 3:
        return "Chill"
    elif num == 4:
        return "Relax"


def random_color():
    """
    This function chooses a random color for the special stop sign.
    :return str, the color for the special stop sign
    """
    num = random.choice(range(9))
    if num == 0:
        return "dodgerblue"
    elif num == 1:
        return "azure"
    elif num == 2:
        return "limegreen"
    elif num == 3:
        return "lavender"
    elif num == 4:
        return "navy"
    elif num == 5:
        return "peachpuff"
    elif num == 6:
        return "orangered"
    elif num == 7:
        return "sage"
    else:
        return "sienna"


def build_background():
    """
    This function creates a rectangle as a background for the window with GRect
    :return: object, background
    """
    back_ground = GRect(800, 500)
    back_ground.filled = True
    back_ground.fill_color = 'silver'
    back_ground.color = 'silver'
    return back_ground


if __name__ == "__main__":
    main()
