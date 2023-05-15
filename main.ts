input.onGesture(Gesture.Shake, function on_gesture_shake() {
    let item = randint(0, 4)
    if (item == 0) {
        basic.showString("honestly no")
    } else if (item == 1) {
        basic.showString("im sorry but no")
    } else if (item == 2) {
        basic.showString("yes for sure")
    } else if (item == 3) {
        basic.showString("without a doubt")
    } else if (item == 4) {
        basic.showString("When pigs fly...")
    }
    
})
