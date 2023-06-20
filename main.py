def on_received_string(receivedString):
    global forw, lspeed, rspeed
    if receivedString == "a":
        forw += 1
    elif receivedString == "b":
        forw += -1
    elif receivedString == "c":
        forw = 0
    elif receivedString == "r":
        lspeed = 0
        rspeed = 20
    elif receivedString == "l":
        rspeed = 0
        lspeed = 20
    elif receivedString == "d":
        rspeed = 0
        lspeed = 0
    basic.pause(1000)
radio.on_received_string(on_received_string)

rspeed = 0
lspeed = 0
forw = 0
radio.set_group(123)
forward = 0
camp = -1
speed = 30
_1 = 100

def on_forever():
    if 0 > forw:
        motor.motor_run(motor.Motors.M1, motor.Dir.CCW, -30 * forw + rspeed)
        motor.motor_run(motor.Motors.M2, motor.Dir.CW, -30 * forw + lspeed)
    else:
        motor.motor_run(motor.Motors.M1, motor.Dir.CW, 30 * forw + rspeed)
        motor.motor_run(motor.Motors.M2, motor.Dir.CCW, 30 * forw + lspeed)
basic.forever(on_forever)
