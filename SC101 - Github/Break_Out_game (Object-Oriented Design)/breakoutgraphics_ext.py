"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This is the graphics package of Ethan's breakout game.

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GPolygon
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MIN_X_SPEED = 3
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # set up the paddle.
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-PADDLE_WIDTH)/2,
                            y=self.window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.paddle.color = 'slategrey'
        self.paddle.fill_color = 'slategrey'

        # set up a the ball.
        self.ball_radius = ball_radius
        self.ball = GOval(self.ball_radius*2, self.ball_radius*2, x=(self.window_width-self.ball_radius*2)/2,
                     y=(self.window_height - self.ball_radius*2)/2)
        self.ball.filled = True
        self.ball.color = 'crimson'
        self.ball.fill_color = 'crimson'

        # Default initial velocity for the ball.
        self.__dx = random.randint(MIN_X_SPEED, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners.
        onmousemoved(self.move_paddle)
        onmouseclicked(self.switch)

        # Control whether the user can start the game
        self.__start = False

        # Determine the lives the user gets
        self.__num_lives = 0

        # Attributes relate to the score
        self.__score = 0
        self.__win_score = BRICK_COLS*BRICK_ROWS*10
        self.score_sign = GLabel(f'SCORE : {self.__score}')
        self.can_move = False
        self.can_drop = True
        self.reward = 0

        # Attribute relate to live sign
        self.live_2 = GOval(self.ball_radius * 2, self.ball_radius * 2,
                            x=self.window_width - (self.ball_radius * 2 + 8), y=self.window_height - (self.ball_radius * 2 + 8))
        self.live_1 = GOval(self.ball_radius * 2, self.ball_radius * 2,
                            x=self.window_width - (self.ball_radius * 2 + 8)*2, y=self.window_height - (self.ball_radius * 2 + 8))

        # Attributes relate to extension opening
        self.o_ball = GOval(30, 30, x=(self.window.width-30)/2, y=240)
        self.start_button = GLabel('S T A R T')
        self.__enter_game = False

        # Attributes relate to extension 'game over' scene
        self.game_over_w = GLabel('G A M E   O V E R')

        # Attributes relate to rewards
        self.hint_sign = 0
        self.reverse_paddle = False
        self.paddle_adding = False
        self.adding_count = 0

        # To store the mouse event
        self.paddle_x = 0

    def set_game(self):
        """
        This method set up the starting interface for the game.
        Including materials such as: paddle, window, score sign and bricks.
        """
        # Create a paddle.
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.window.add(self.ball)

        # Build the score sign
        self.score_sign = GLabel(f'SCORE : {self.__score}')
        self.score_sign.color = 'crimson'
        self.score_sign.font = 'Mamelon-20'
        self.window.add(self.score_sign, x=8, y=self.window.height-8)

        # Build lives sign
        self.live_2.filled = True
        self.live_2.color = 'crimson'
        self.live_2.fill_color = 'crimson'
        self.window.add(self.live_2)

        self.live_1.filled = True
        self.live_1.color = 'crimson'
        self.live_1.fill_color = 'crimson'
        self.window.add(self.live_1)

        # Draw bricks.
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=i * (BRICK_WIDTH + BRICK_SPACING),
                              y=BRICK_OFFSET + j * (BRICK_HEIGHT + BRICK_SPACING))
                brick.filled = True
                if j == 0 or j == 1:
                    brick.color = 'darkslategrey'
                    brick.fill_color = 'darkslategrey'
                elif j == 2 or j == 3:
                    brick.color = 'teal'
                    brick.fill_color = 'teal'
                elif j == 4 or j == 5:
                    brick.color = 'cadetblue'
                    brick.fill_color = 'cadetblue'
                elif j == 6 or j == 7:
                    brick.color = 'lightseagreen'
                    brick.fill_color = 'lightseagreen'
                else:
                    brick.color = 'mediumturquoise'
                    brick.fill_color = 'mediumturquoise'
                self.window.add(brick)

    def move_paddle(self, event):
        """
        This method keep mouse event regarding reverse and not reverse situation of the paddle.
        Also, it keeps the paddle within the window .
        :param event: mouse event
        """
        if self.reverse_paddle:
            # reverse paddle movement
            event_x = self.window_width - event.x
        else:
            # Normal paddle movement
            event_x = event.x

        # Keeping the paddle within the window
        if event_x - self.paddle_width/2 < 0:
            self.paddle.x = 0
        elif event_x + self.paddle_width/2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle_width

        # Control the paddle when the mouse is in the window
        else:
            self.paddle.x = event_x - self.paddle_width/2

        # To store the mouse event
        self.paddle_x = self.paddle.x

    def reset_ball(self):
        """
        This method resets the ball at the starting position,
        and will not drop unless the the user clicks.
        """
        self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2, x=(self.window_width - self.ball_radius * 2) / 2,
                          y=(self.window_height - self.ball_radius * 2) / 2)
        self.ball.filled = True
        self.ball.color = 'crimson'
        self.ball.fill_color = 'crimson'
        self.window.add(self.ball)
        self.__start = False

    # getter for the ball's moving speed.
    def get_dx(self):
        return self.__dx

    # getter for the ball's moving speed.
    def get_dy(self):
        return self.__dy

    # getter, see if the ball is ready to be click and fall
    def start(self):
        return self.__start

    # getter, see if the start button in the opening scene is clicked
    def get_enter_game(self):
        return self.__enter_game

    # setter, the user can set up the initial lives.
    def set_num_lives(self, num_lives):
        self.__num_lives = num_lives

    def switch(self, e):
        """
        This method is the switch for 2 purpose.

        1. whether the user can start the game.
        In the start of each round, if user's lives > 0, the switch will set to open,
        the ball will move after the user click the window.

        2. whether the start button in the opening scene is clicked.
        If clicked, set up the game.
        If not, wait for the click.
        """
        if self.__num_lives > 0:
            self.__start = True

        if self.window.get_object_at(e.x, e.y) is self.o_ball or \
                self.window.get_object_at(e.x, e.y) is self.start_button:
            self.__enter_game = True

    # To get the position of the 4 corners of the ball
    def corner_hits(self):
        """
        This method check from corner_1 to corner_4,
        to see if any corner of the ball has encounter obstacles.

        If so, return the method to remove object encountered.
        If not, move on to the next corner.

        :return: method, remove the object on the encountered corner.
        """
        # To get position of each corner of the ball
        corner_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        corner_2 = self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y)
        corner_3 = self.window.get_object_at(self.ball.x, self.ball.y+2*self.ball_radius)
        corner_4 = self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y+2*self.ball_radius)

        # To check which corner hits things
        if corner_1 is not None:
            return corner_1
        elif corner_2 is not None:
            return corner_2
        elif corner_3 is not None:
            return corner_3
        elif corner_4 is not None:
            return corner_4
        else:
            pass

    # To check whether the ball hits the wall
    def if_hits_walls(self):
        """
        This method checks whether the ball hits the side walls and the the top wall.
        If so, the ball will bounce back.
        """
        # The ball hits the side walls and the the top wall
        if self.ball.x <= 0 or self.ball.x + 2 * self.ball_radius >= self.window.width:
            self.__dx *= -1
        # The ball hits the the top wall
        if self.ball.y <= 0:
            self.__dy *= -1

    # To check what the ball hits
    def if_hits_things(self):
        """
        This method determines what kind of object the ball hits,
        and run the actions after hitting certain objects.
        """
        # The ball hits the paddle
        if self.corner_hits() is self.paddle:
            # bounce back
            if self.__dy >= 0:
                self.__dy *= -1
            else:
                # debug: keep the ball from sticking on the paddle
                pass
            # Clean up the hint sign
            self.window.remove(self.hint_sign)

        # the ball hits other item, pass
        elif self.corner_hits() is self.score_sign or self.corner_hits() is self.hint_sign or self.corner_hits() is self.reward \
                or self.corner_hits() is self.live_2 or self.corner_hits() is self.live_1:
            pass

        # The ball hits the paddle
        elif self.corner_hits() is not None:

            # The thing hit by the ball need to be removed
            self.window.remove(self.corner_hits())

            # Speed up and bounce
            self.__dy *= -1.005
            self.__score += 10

            # Show score
            self.show_score()

            # The reward will dropped everytime the user get 70 more score.
            if self.__score % 70 == 0 and self.can_drop:

                # Choose the dropping x position randomly
                t_x = random.choice(range(1,10))

                # Set up the reward object
                self.reward = GRect(10, 10, x=self.window.width*t_x//10, y=self.window.height/3)
                self.reward.filled = True
                self.reward.fill_color = 'darkslateblue'
                self.reward.color = 'darkslateblue'
                self.window.add(self.reward)
                self.can_move = True
        else:
            pass

    def show_score(self):
        """
        This method remove the previous score sign and create a new one.
        """
        self.window.remove(self.score_sign)
        self.score_sign = GLabel(f'SCORE : {self.__score}')
        self.score_sign.color = 'crimson'
        self.score_sign.font = 'Mamelon-20'
        self.window.add(self.score_sign, x=8, y=self.window.height-8)

    # To check: if the reward is allowed to drop / if it was obtained or missed.
    def test_move(self):
        if self.can_move:
            self.can_drop = False
            self.reward.move(0, 5)

            # The user got the reward
            if self.window.get_object_at(self.reward.x+7, self.reward.y+15) is self.paddle:
                self.window.remove(self.reward)
                self.run_reward()
                self.can_move = False
                self.can_drop = True

            # The user miss the reward -- clean up
            if self.reward.y+15 >= self.window.height:
                self.window.remove(self.reward)
                self.can_move = False
                self.can_drop = True

    def run_reward(self):
        """
        This method uses random to choose a reward to run randomly.
        Also, it shows a sign for the running reward.

        Possible situation are listed below:
        1. Make the paddle longer
        2. Make the paddle shorter
        3. Reverse the paddle's movement
        4. Speed up the ball
        5. Slow down the ball
        """
        # Choose a reward randomly
        choice = random.choice(range(6))
        self.window.remove(self.hint_sign)

        # paddle width ++
        if choice == 0:
            self.window.remove(self.paddle)
            self.paddle_width += 20
            self.paddle = GRect(self.paddle_width, self.paddle_height, x=self.paddle_x-self.paddle_width/2,
                                    y=self.window_height - PADDLE_OFFSET - self.paddle_height)
            self.build_paddle()
            self.hint_sign = GLabel('ADD UP')
            self.show_hint()

        # paddle width --
        elif choice == 1:
            self.paddle_adding = False
            if self.paddle_width <= 30:
                pass
            else:
                self.window.remove(self.paddle)
                self.paddle_width -= 30
                self.paddle = GRect(self.paddle_width, self.paddle_height, x=self.paddle_x - self.paddle_width / 2,
                                    y=self.window_height - PADDLE_OFFSET - self.paddle_height)
                self.build_paddle()
                self.hint_sign = GLabel('WATCH OUT')
                self.show_hint()

        # Set reverse paddle movement
        elif choice == 2 or choice == 3:
            if self.reverse_paddle:
                self.reverse_paddle = False
                self.hint_sign = GLabel('REVERSE AGAIN')
                self.show_hint()
            else:
                self.reverse_paddle = True
                self.hint_sign = GLabel('REVERSE')
                self.show_hint()

        # Speed up the ball
        elif choice == 4:
            self.__dy *= 1.1
            self.hint_sign = GLabel('SPEED UP')
            self.show_hint()

        # Slow down the ball
        else:
            self.__dy *= 0.9
            self.hint_sign = GLabel('SLOW DOWN')
            self.show_hint()

    def build_paddle(self):
        """
        This methods build up paddle for each reward.
        """
        self.window.add(self.paddle)
        self.paddle.filled = True
        self.paddle.color = 'slategrey'
        self.paddle.fill_color = 'slategrey'

    def show_hint(self):
        """
        This method shows a sign to tell user that clicking can earn rewards
        """
        self.hint_sign.color = 'crimson'
        self.hint_sign.font = 'Mamelon-20'
        self.window.add(self.hint_sign, x=(self.window.width-self.hint_sign.width)/2,
                        y=self.window_height-PADDLE_OFFSET-PADDLE_HEIGHT-30)

    def if_lose_life(self):
        """
        This method check if the user lost life.
        If so, will reset the ball if there's still lives remain.
        """
        if self.ball.y >= self.window.height:
            self.window.remove(self.ball)
            self.window.remove(self.hint_sign)
            self.__num_lives -= 1

            if self.__num_lives == 2:
                # Build 1 point
                self.window.remove(self.live_1)

            elif self.__num_lives == 1:
                # empty
                self.window.remove(self.live_2)

            # Avoid being too hard for players to get ball with reverse paddle
            self.reverse_paddle = False
            self.__dy = INITIAL_Y_SPEED

            if self.__num_lives > 0:
                # User still has chances
                self.reset_ball()

    # Getter, to check if it's the end of the game (either win or lose)
    def end_game(self):
        if self.__num_lives <= 0 or self.__score >= self.__win_score:
            return True

    # To check if the game is over
    def game_over(self):
        if self.__num_lives <= 0:
            self.__enter_game = False
            return True

    def build_game_over(self):
        """
        This method builds the 'Game Over' scene
        """

        # delete the score
        line = GLine(4, self.window.height - 18, 12 + self.score_sign.width, self.window.height - 18)
        line.color = 'crimson'
        self.window.add(line)

        # Clean up
        self.window.remove(self.reward)
        self.window.remove(self.hint_sign)

        # Build up the 'Game Over' sign
        self.game_over_w.font = "Mamelon-35"
        self.game_over_w.color = 'midnightblue'
        self.window.add(self.game_over_w, x=(self.window.width - self.game_over_w.width) / 2, y = self.window.height/2)

        # Create the movement of the 'Game Over' sign
        speed = self.__dy
        while True:
            self.game_over_w.move(0, speed)
            speed += 0.5
            if self.game_over_w.y >= self.window.height*2//3:
                speed *= -0.7
            pause(10)
        # The sign will end with a shaking animation.

    # To check if the user won the game
    def win_game(self):
        if self.__score >= self.__win_score:
            return True

    def build_win(self):
        """
        This method builds the 'Winning' scene
        """
        win_sign_1 = GLabel('S A V A G E')
        win_sign_1.font = 'Mamelon-40'
        win_sign_1.color = 'mediumturquoise'
        win_sign_2 = GLabel('S A V A G E')
        win_sign_2.font = 'Mamelon-40'
        win_sign_2.color = 'mediumturquoise'
        win_sign_3 = GLabel('S A V A G E')
        win_sign_3.font = 'Mamelon-40'
        win_sign_3.color = 'mediumturquoise'

        # To create the flashing animation
        for i in range(12):
            if i % 2 != 0:
                self.window.add(win_sign_1, x=(self.window.width-win_sign_1.width)/2, y=(self.window.height-win_sign_1.height)/2)
                self.window.add(win_sign_2, x=(self.window.width - win_sign_2.width) / 2, y=(self.window.height - win_sign_2.height) / 2+50)
                self.window.add(win_sign_3, x=(self.window.width - win_sign_3.width) / 2, y=(self.window.height - win_sign_3.height) / 2+100)
            else:
                self.window.remove(win_sign_1)
                self.window.remove(win_sign_2)
                self.window.remove(win_sign_3)

            pause(100)

        self.fire_work()

    def fire_work(self):
        """
        This method creates a firework animation.
        """

        # Numbers of the firework
        for i in range(10):
            f_x = random.randint(self.window.width // 8, self.window.width * 7 // 8)
            f_y = random.randint(self.window.height // 10, self.window.height * 9 // 10)
            size = random.randint(4, 7)

            # The size of the firework
            for j in range(size):
                fire = GOval(10+20*j, 10+20*j, x=f_x-10*j, y=f_y-10*j)

                # Choose color randomly
                fire.color = self.choose_color()
                self.window.add(fire)
                pause(100)

                self.window.remove(fire)

            pause(500)

    @staticmethod
    def choose_color():
        """
        This method help choose the color for each circle of the firework randomly
        """
        num = random.choice(range(6))
        if num == 0:
            return "crimson"
        elif num == 1:
            return "midnightblue"
        elif num == 2:
            return "limegreen"
        elif num == 3:
            return "cyan"
        elif num == 4:
            return 'darkviolet'
        else:
            return "gold"

    def window_clear(self):
        """
        This method clean up the whole window after the opening scene is over.
        """
        self.window.clear()

    def set_opening(self):
        """
        This method set up the whole opening scene.
        """

        # To create the tube
        start_button_1 = GRect(60, 211, x=(self.window.width-60)/2, y=-1)
        start_button_1.color = 'slategrey'
        start_button_1.filled = True
        start_button_1.fill_color = 'slategrey'
        start_button_2 = GRect(50, 206, x=(self.window.width-50)/2)
        start_button_2.color = 'gainsboro'
        start_button_2.filled = True
        start_button_2.fill_color = 'gainsboro'
        self.window.add(start_button_1)
        self.window.add(start_button_2)
        head = GPolygon()
        head.add_vertex(((self.window.width-60)/2, 210))
        head.add_vertex(((self.window.width-60)/2+60, 210))
        head.add_vertex(((self.window.width-60)/2+60+20, 240))
        head.add_vertex(((self.window.width-60)/2-20, 240))
        head.color = 'slategrey'
        head.filled = True
        head.fill_color = 'slategrey'
        self.window.add(head)

        # Loading animation
        for i in range(10):
            load = GRect(40, 15, x=(self.window.width-60)/2+10, y=5+20*i)
            load.filled = 'True'
            load.color = 'slategrey'
            load.fill_color = 'slategrey'
            self.window.add(load)
            pause(100)

        # Bouncing ball
        self.o_ball.filled = 'True'
        self.o_ball.color = 'crimson'
        self.o_ball.fill_color = 'crimson'
        self.window.add(self.o_ball)
        ball_vy = 5
        count = 0
        while True:
            self.o_ball.move(0, ball_vy)
            ball_vy += 1
            if self.o_ball.y+30 >= self.window.height:
                ball_vy *= -0.9
                count += 1
            if count == 5 and ball_vy >= 0:
                break
            pause(10)
        self.window.remove(self.o_ball)

        # Blowing balloon animation
        for i in range(55):
            self.o_ball = GOval(30+i, 30+i, x=(self.window.width-30+i)/2-i, y=415-i)
            self.o_ball.filled = 'True'
            self.o_ball.color = 'crimson'
            self.o_ball.fill_color = 'crimson'
            self.window.add(self.o_ball)
            pause(7)

        # Flashing start sign animation
        for i in range(10):
            self.start_button.font = 'Mamelon-20'
            if i % 2 == 0:
                self.start_button.color = 'crimson'
            else:
                self.start_button.color = 'snow'
            self.window.add(self.o_ball)
            self.window.add(self.start_button, x=(self.window.width-64)/2, y=413)
            pause(100)

        # Show the rules
        rule_1 = GLabel('3 LIVES.')
        rule_1.color = 'darkslategrey'
        rule_1.font = 'Mamelon-20'
        rule_2 = GLabel("CATCH '    ' FOR RANDOM EFFECTS.")
        rule_2.color = 'darkslategrey'
        rule_2.font = 'Mamelon-20'
        rule_3 = GLabel('SCORE 1000 ---> FIREWORKS.')
        rule_3.color = 'crimson'
        rule_3.font = 'Mamelon-20'
        square = GRect(10, 10, x=self.window.width/10+63, y=self.window.height*4//5+10)
        square.filled = True
        square.fill_color = 'darkslateblue'
        square.color = 'darkslateblue'
        self.window.add(square)
        self.window.add(rule_1, x=self.window.width/10, y=self.window.height*4//5)
        self.window.add(rule_2, x=self.window.width/10, y=self.window.height*4//5+25)
        self.window.add(rule_3, x=self.window.width/10, y=self.window.height*4//5+50)



