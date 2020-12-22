"""
This is Ethan's breakOut Game!

Rules:
1. Player gets three lives.
2. Get dropping square for special bonus.
3. Score 1000 to win and unlock fireworks animation!


Designs:
1. When player catch the bonus,
    the program chooses an effect randomly
    -- including longer/shorten/reverse the paddle and speed up/slow down the ball.

2. Each time when the ball hits a brick, it speeds up for 1.005 time

3. When the player lost a life,
    special effects and the ball's speed return to initial setting.


HAVE FUN!

"""

from breakoutgraphics_ext import BreakoutGraphics
from campy.gui.events.timer import pause

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    graphics.window_clear()
    graphics.set_opening()

    while True:
        if graphics.get_enter_game():
            # 按了start才進到遊戲

            graphics.window_clear()
            graphics.set_num_lives(NUM_LIVES)
            graphics.set_game()

            # Add animation loop here!
            while True:
                pause(FRAME_RATE)
                if graphics.start():
                    graphics.ball.move(graphics.get_dx(), graphics.get_dy())
                    graphics.if_hits_walls()
                    graphics.if_hits_things()
                    graphics.if_lose_life()
                graphics.test_move()

                if graphics.end_game():
                    break
            break

        pause(FRAME_RATE)

    # Check if the game is over
    if graphics.game_over():
        graphics.build_game_over()

    # Check if win game
    if graphics.win_game():
        graphics.build_win()


pause(FRAME_RATE)
if __name__ == '__main__':
    main()
