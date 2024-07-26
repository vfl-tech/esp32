from machine import Pin
from time import sleep

segments = {
    'a': Pin(2, Pin.OUT),
    'b': Pin(4, Pin.OUT),
    'c': Pin(18, Pin.OUT),
    'd': Pin(19, Pin.OUT),
    'e': Pin(21, Pin.OUT),
    'f': Pin(22, Pin.OUT),
    'g': Pin(23, Pin.OUT),

}

digits = {
    '0': ['a', 'b', 'c', 'd', 'e', 'f'],
    '1': ['b', 'c'],
    '2': ['a', 'b', 'd', 'e', 'g'],
    '3': ['a', 'b', 'c', 'd', 'g'],
    '4': ['b', 'c', 'f', 'g'],
    '5': ['a', 'c', 'd', 'f', 'g'],
    '6': ['a', 'c', 'd', 'e', 'f', 'g'],
    '7': ['a', 'b', 'c'],
    '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    '9': ['a', 'b', 'c', 'd', 'f', 'g']
}

def display_digit(digit):
    for segment in segments.values():
        segment.value(0)
    for segment in digits[digit]:
        segments[segment].value(1)

while True:
    for digit in '0123456789':
        display_digit(digit)
        sleep(1)


