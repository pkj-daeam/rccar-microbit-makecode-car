def on_received_number(receivedNumber):
    global camp
    camp = receivedNumber
radio.on_received_number(on_received_number)

def on_received_string(receivedString):
    global forward, forw
    if receivedString == "a":
        forward = 1
    elif receivedString == "b":
        forward = 2
    else:
        forw = 0
radio.on_received_string(on_received_string)

forw = 0
camp = 0
forward = 0
radio.set_group(123)
forward = 0
camp = 0
speed = 0
_1 = 100

def on_forever():
    if input.compass_heading() - 180 > camp - 180:
        motor.motor_run(motor.Motors.M1, motor.Dir.CW, _1)
        motor.motor_run(motor.Motors.M2, motor.Dir.CW, _1)
    elif input.compass_heading() - 180 == camp - 180:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    else:
        motor.motor_run(motor.Motors.M1, motor.Dir.CCW, _1)
        motor.motor_run(motor.Motors.M2, motor.Dir.CCW, _1)
    if forward == 1:
        motor.motor_run(motor.Motors.M1, motor.Dir.CW, speed)
        motor.motor_run(motor.Motors.M2, motor.Dir.CCW, speed)
    if forward == 2:
        motor.motor_run(motor.Motors.M1, motor.Dir.CCW, speed)
        motor.motor_run(motor.Motors.M2, motor.Dir.CW, speed)
basic.forever(on_forever)
