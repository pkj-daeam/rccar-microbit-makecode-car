radio.onReceivedString(function (receivedString) {
    if (receivedString == "a") {
        forw += 1
    } else if (receivedString == "b") {
        forw += -1
    } else if (receivedString == "c") {
        forw = 0
    } else if (receivedString == "r") {
        lspeed = 0
        rspeed = 20
    } else if (receivedString == "l") {
        rspeed = 0
        lspeed = 20
    } else if (receivedString == "d") {
        rspeed = 0
        lspeed = 0
    }
    basic.pause(1000)
})
let rspeed = 0
let lspeed = 0
let forw = 0
let forward = 0
radio.setGroup(123)
let camp = -1
let speed = 30
let _1 = 100
basic.forever(function () {
    if (0 >= forw) {
        motor.MotorRun(motor.Motors.M1, motor.Dir.CCW, -30 * forw + rspeed)
        motor.MotorRun(motor.Motors.M2, motor.Dir.CW, -30 * forw + lspeed)
    } else {
        motor.MotorRun(motor.Motors.M1, motor.Dir.CW, 30 * forw + rspeed)
        motor.MotorRun(motor.Motors.M2, motor.Dir.CCW, 30 * forw + lspeed)
    }
})
