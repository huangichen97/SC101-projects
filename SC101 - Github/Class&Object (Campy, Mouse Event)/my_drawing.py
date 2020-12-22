"""
File: my_drawing.py
Name: Ethan Huang
----------------------
TODO:
This program is a drawing I create for the drawing competition of StanCode101
It builds an interface from the background to the front layer,
mimicking the "Kahoot" game to ask users to choose the real Karel.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GLine
from campy.graphics.gwindow import GWindow

window = GWindow(800, 550, title='Which One IS Karel?')


def main():
    """
    TODO:
    This program builds an interface from the background to the front layer,
    from background to blocks, karels and texts.
    """
    build_background()
    build_blocks()
    build_karels()
    build_labels()


def build_background():
    """
    This function builds the background of the drawing with three parts.
    """
    layer_1 = GRect(800, 550)
    layer_1.filled = True
    layer_1.color = 'silver'
    layer_1.fill_color = 'silver'
    window.add(layer_1)
    layer_2 = GRect(800, 90)
    layer_2.filled = True
    layer_2.color = 'whitesmoke'
    layer_2.fill_color = 'whitesmoke'
    window.add(layer_2)
    layer_3 = GRect(800, 40, x=0, y=510)
    layer_3.filled = True
    layer_3.color = 'whitesmoke'
    layer_3.fill_color = 'whitesmoke'
    window.add(layer_3)


def build_blocks():
    """
    This function builds the blocks of the drawing
    """
    block_1 = GRect(375, 80, x=20, y=330)
    block_1.filled = True
    block_1.color = 'firebrick'
    block_1.fill_color = 'firebrick'
    window.add(block_1)
    block_2 = GRect(375, 80, x=405, y=330)
    block_2.filled = True
    block_2.color = 'steelblue'
    block_2.fill_color = 'steelblue'
    window.add(block_2)
    block_3 = GRect(375, 80, x=20, y=420)
    block_3.filled = True
    block_3.color = 'goldenrod'
    block_3.fill_color = 'goldenrod'
    window.add(block_3)
    block_4 = GRect(375, 80, x=405, y=420)
    block_4.filled = True
    block_4.color = 'forestgreen'
    block_4.fill_color = 'forestgreen'
    window.add(block_4)
    block_5 = GRect(60, 40, x=720, y=120)
    block_5.filled = True
    block_5.color = 'dodgerblue'
    block_5.fill_color = 'dodgerblue'
    window.add(block_5)
    circle_1 = GOval(90, 90, x=20, y=170)
    circle_1.filled = True
    circle_1.color = 'blueviolet'
    circle_1.fill_color = 'blueviolet'
    window.add(circle_1)


def build_karels():
    """
    This function builds four Karels
    """
    build_karel1()
    build_karel2()
    build_karel3()
    build_karel4()


def build_karel1():
    """
    This function builds the first karel
    """
    head = GOval(80, 55, x=190, y=167)
    head.filled = True
    head.color = 'black'
    head.fill_color = 'gray'
    window.add(head)
    r_eye = GRect(13, 13, x=212, y=189)
    r_eye.filled = True
    r_eye.color = 'black'
    r_eye.fill_color = 'blue'
    window.add(r_eye)
    l_eye = GRect(13, 13, x=235, y=189)
    l_eye.filled = True
    l_eye.color = 'black'
    l_eye.fill_color = 'blue'
    window.add(l_eye)
    r_eyeb = GLine(212, 185, 225, 185)
    window.add(r_eyeb)
    l_eyeb = GLine(235, 185, 248, 185)
    window.add(l_eyeb)
    hands = GRect(105, 45, x=177, y=237)
    hands.filled = True
    hands.color = 'black'
    hands.fill_color = 'lime'
    window.add(hands)
    body_1 = GRect(60, 65, x=201, y=223)
    body_1.filled = True
    body_1.color = 'black'
    body_1.fill_color = 'blue'
    window.add(body_1)
    body_2 = GRect(80, 60, x=190, y=230)
    body_2.filled = True
    body_2.color = 'black'
    body_2.fill_color = 'blue'
    window.add(body_2)
    r_foot = GOval(29, 24, x=190, y=290)
    r_foot.filled = True
    r_foot.color = 'black'
    r_foot.fill_color = 'red'
    window.add(r_foot)
    l_foot = GOval(29, 24, x=241, y=290)
    l_foot.filled = True
    l_foot.color = 'black'
    l_foot.fill_color = 'red'
    window.add(l_foot)
    label = GPolygon()
    label.add_vertex((230, 130))
    label.add_vertex((218, 150))
    label.add_vertex((242, 150))
    label.filled = True
    label.fill_color = 'firebrick'
    label.color = 'firebrick'
    window.add(label)


def build_karel2():
    """
    This function builds the second karel
    """
    add = 1
    head = GOval(80, 55, x=190+120*add, y=167)
    head.filled = True
    head.color = 'black'
    head.fill_color = 'gray'
    window.add(head)
    r_eye = GRect(13, 13, x=212+120*add, y=189)
    r_eye.filled = True
    r_eye.color = 'black'
    r_eye.fill_color = 'blue'
    window.add(r_eye)
    l_eye = GRect(13, 13, x=235+120*add, y=189)
    l_eye.filled = True
    l_eye.color = 'black'
    l_eye.fill_color = 'blue'
    window.add(l_eye)
    mouth = GPolygon()
    mouth.filled = True
    mouth.fill_color = 'red'
    mouth.color = 'black'
    mouth.add_vertex((350, 205))
    mouth.add_vertex((353, 211))
    mouth.add_vertex((347, 211))
    window.add(mouth)
    hands = GRect(105, 45, x=177+120*add, y=237)
    hands.filled = True
    hands.color = 'black'
    hands.fill_color = 'lime'
    window.add(hands)
    body_1 = GRect(60, 65, x=201+120*add, y=223)
    body_1.filled = True
    body_1.color = 'black'
    body_1.fill_color = 'blue'
    window.add(body_1)
    body_2 = GRect(80, 60, x=190+120*add, y=230)
    body_2.filled = True
    body_2.color = 'black'
    body_2.fill_color = 'blue'
    window.add(body_2)
    r_foot = GOval(29, 24, x=190+120*add, y=290)
    r_foot.filled = True
    r_foot.color = 'black'
    r_foot.fill_color = 'red'
    window.add(r_foot)
    l_foot = GOval(29, 24, x=241+120*add, y=290)
    l_foot.filled = True
    l_foot.color = 'black'
    l_foot.fill_color = 'red'
    window.add(l_foot)
    label1 = GPolygon()
    label1.add_vertex((230+120*add, 128))
    label1.add_vertex((218+120*add, 140))
    label1.add_vertex((242+120*add, 140))
    label1.filled = True
    label1.fill_color = 'steelblue'
    label1.color = 'steelblue'
    window.add(label1)
    label2 = GPolygon()
    label2.add_vertex((230 + 120 * add, 152))
    label2.add_vertex((218 + 120 * add, 140))
    label2.add_vertex((242 + 120 * add, 140))
    label2.filled = True
    label2.fill_color = 'steelblue'
    label2.color = 'steelblue'
    window.add(label2)


def build_karel3():
    """
    This function builds the third karel
    """
    add = 2
    head = GOval(80, 55, x=190 + 120 * add, y=167)
    head.filled = True
    head.color = 'black'
    head.fill_color = 'gray'
    window.add(head)
    r_eye = GRect(13, 13, x=212 + 120 * add, y=189)
    r_eye.filled = True
    r_eye.color = 'black'
    r_eye.fill_color = 'blue'
    window.add(r_eye)
    l_eye = GRect(13, 13, x=235 + 120 * add, y=189)
    l_eye.filled = True
    l_eye.color = 'black'
    l_eye.fill_color = 'blue'
    window.add(l_eye)
    hands = GRect(105, 45, x=177 + 120 * add, y=237)
    hands.filled = True
    hands.color = 'black'
    hands.fill_color = 'lime'
    window.add(hands)
    body_1 = GRect(60, 65, x=201 + 120 * add, y=223)
    body_1.filled = True
    body_1.color = 'black'
    body_1.fill_color = 'blue'
    window.add(body_1)
    body_2 = GRect(80, 60, x=190 + 120 * add, y=230)
    body_2.filled = True
    body_2.color = 'black'
    body_2.fill_color = 'blue'
    window.add(body_2)
    r_foot = GOval(29, 24, x=190 + 120 * add, y=290)
    r_foot.filled = True
    r_foot.color = 'black'
    r_foot.fill_color = 'red'
    window.add(r_foot)
    l_foot = GOval(29, 24, x=241 + 120 * add, y=290)
    l_foot.filled = True
    l_foot.color = 'black'
    l_foot.fill_color = 'red'
    window.add(l_foot)
    label = GOval(22, 22, x=218+120*add, y=130)
    label.filled = True
    label.fill_color = 'goldenrod'
    label.color = 'goldenrod'
    window.add(label)


def build_karel4():
    """
    This function builds the fourth karel
    """
    add = 3
    head = GOval(80, 55, x=190 + 120 * add, y=167)
    head.filled = True
    head.color = 'black'
    head.fill_color = 'gray'
    window.add(head)
    hair1 = GLine(590, 167, 590, 161)
    hair2 = GLine(588, 168, 585, 162)
    hair3 = GLine(592, 168, 595, 162)
    hair4 = GLine(585, 168, 582, 162)
    hair5 = GLine(595, 168, 598, 162)
    window.add(hair1)
    window.add(hair2)
    window.add(hair3)
    window.add(hair4)
    window.add(hair5)
    r_eye = GOval(14, 14, x=212 + 120 * add, y=189)
    r_eye.filled = True
    r_eye.color = 'black'
    r_eye.fill_color = 'blue'
    window.add(r_eye)
    l_eye = GOval(14, 14, x=235 + 120 * add, y=189)
    l_eye.filled = True
    l_eye.color = 'black'
    l_eye.fill_color = 'blue'
    window.add(l_eye)
    hands = GRect(105, 45, x=177 + 120 * add, y=237)
    hands.filled = True
    hands.color = 'black'
    hands.fill_color = 'lime'
    window.add(hands)
    body_1 = GRect(60, 65, x=201 + 120 * add, y=223)
    body_1.filled = True
    body_1.color = 'black'
    body_1.fill_color ='blue'
    window.add(body_1)
    body_2 = GRect(80, 60, x=190 + 120 * add, y=230)
    body_2.filled = True
    body_2.color = 'black'
    body_2.fill_color = 'blue'
    window.add(body_2)
    r_foot = GOval(29, 24, x=190 + 120 * add, y=290)
    r_foot.filled = True
    r_foot.color = 'black'
    r_foot.fill_color = 'red'
    window.add(r_foot)
    l_foot = GOval(29, 24, x=241 + 120 * add, y=290)
    l_foot.filled = True
    l_foot.color = 'black'
    l_foot.fill_color = 'red'
    window.add(l_foot)
    label = GRect(20, 20, x=218+120*add, y=130)
    label.filled = True
    label.fill_color = 'forestgreen'
    label.color = 'forestgreen'
    window.add(label)


def build_labels():
    """
    This function creates the texts on the canvas
    """
    l_title = GLabel('Which one is Karel?')
    l_title.font = 'Courier-25'
    l_title.color = 'black'
    window.add(l_title, x=260, y=60)
    l_num = GLabel('19')
    l_num.font = 'Courier-50'
    l_num.color = 'whitesmoke'
    window.add(l_num, x=37, y=242)
    l_skip = GLabel('skip')
    l_skip.font = 'Courier-20'
    l_skip.color = 'whitesmoke'
    window.add(l_skip, x=726, y=152)
    l_ans1 = GLabel('Answers')
    l_ans1.font = 'Courier-20-italic'
    l_ans1.color = 'black'
    window.add(l_ans1, x=698, y=270)
    l_ans2 = GLabel('0')
    l_ans2.font = 'Courier-50-italic'
    l_ans2.color = 'black'
    window.add(l_ans2, x=722, y=252)
    l_game_pin = GLabel('Game PIN: SC101')
    l_game_pin.font = 'Courier-20'
    l_game_pin.color = 'black'
    window.add(l_game_pin, x=20, y=540)
    l_1 = GPolygon()
    l_1.add_vertex((210, 360))
    l_1.add_vertex((197, 380))
    l_1.add_vertex((221, 380))
    l_1.filled = True
    l_1.color = 'whitesmoke'
    l_1.fill_color= 'whitesmoke'
    window.add(l_1)
    l_2_1 = GPolygon()
    l_2_1.add_vertex((210+380, 359))
    l_2_1.add_vertex((198+380, 370))
    l_2_1.add_vertex((221+380, 370))
    l_2_1.filled = True
    l_2_1.fill_color = 'whitesmoke'
    l_2_1.color = 'whitesmoke'
    window.add(l_2_1)
    l_2_2 = GPolygon()
    l_2_2.add_vertex((210+380, 381))
    l_2_2.add_vertex((198+380, 370))
    l_2_2.add_vertex((221+380, 370))
    l_2_2.filled = True
    l_2_2.fill_color = 'whitesmoke'
    l_2_2.color = 'whitesmoke'
    window.add(l_2_2)
    l_3 = GOval(23, 23, x=198, y=450)
    l_3.filled = True
    l_3.fill_color = 'whitesmoke'
    l_3.color = 'whitesmoke'
    window.add(l_3)
    l_4 = GRect(20, 20, x=583, y=450)
    l_4.filled = True
    l_4.fill_color = 'whitesmoke'
    l_4.color = 'whitesmoke'
    window.add(l_4)


if __name__ == '__main__':
    main()
