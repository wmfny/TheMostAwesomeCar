import time

import RPi.GPIO as GPIO

mode = GPIO.getmode()

GPIO.cleanup()

left_forward = 26
left_backward = 19
right_forward = 16
right_backward = 13
sleep_time = 1

pwm_frequency = 200

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_forward, GPIO.OUT)
GPIO.setup(left_backward, GPIO.OUT)
GPIO.setup(right_forward, GPIO.OUT)
GPIO.setup(right_backward, GPIO.OUT)

forwardAmount = 1
reverseAmount = 1
leftAmount = 0.75
rightAmount = 0.75

def forward(x):
    GPIO.output(left_forward, GPIO.HIGH)
    GPIO.output(right_forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(left_forward, GPIO.LOW)
    GPIO.output(right_forward, GPIO.LOW)


def reverse(x):
    GPIO.output(left_backward, GPIO.HIGH)
    GPIO.output(right_backward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(left_backward, GPIO.LOW)
    GPIO.output(right_backward, GPIO.LOW)
    
def left(x):
    GPIO.output(right_forward, GPIO.HIGH)
    GPIO.output(left_backward, GPIO.HIGH)
    print("Turning left")
    time.sleep(x)
    GPIO.output(right_forward, GPIO.LOW)
    GPIO.output(left_backward, GPIO.LOW)
    
def right(x):
    GPIO.output(right_backward, GPIO.HIGH)
    GPIO.output(left_forward, GPIO.HIGH)
    print("Turning Right")
    time.sleep(x)
    GPIO.output(right_backward, GPIO.LOW)
    GPIO.output(left_forward, GPIO.LOW)
    
def execute(response):
    if response == "warm":
        forward(forwardAmount)
    else:
        left(leftAmount)
    
def test_pwm():
    left = GPIO.PWM(left_forward, pwm_frequency)
    right = GPIO.PWM(right_forward, pwm_frequency)
    left.start(0)
    right.start(0)
    try:
        for dc in range(0, 101):
            left.ChangeDutyCycle(dc)
            right.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -1):
            right.ChangeDutyCycle(dc)
            left.ChangeDutyCycle(dc)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    left.stop()
    right.stop()


while 1:
    #forward(0.75)
    #reverse(0.75)
    #time.sleep(1)
    #left(0.25)
    #right(0.5)
    resp = input("warm or not: ")
    if (resp == "quit")
        GPIO.cleanup()
        break
    else
        execute(resp)
        #test_pwm()
