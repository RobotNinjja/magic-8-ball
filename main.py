def on_gesture_shake():
    item = randint(0, 4)
    if item == 0:
     basic.show_string("honestly no")
    elif item == 1:
     basic.show_string("im sorry but no")
    elif item == 2:
     basic.show_string("yes for sure")
    elif item == 3:
      basic.show_string("without a doubt")
    elif item == 4:
        basic.show_string("When pigs fly...")

input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    
 basic.forever(on_forever)
