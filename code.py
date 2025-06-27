from adafruit_circuitplayground import cp
import time  # Write your code here :-)

# Chad Collard
# cpx5-1
# 6/27/2025
# MAX 322

MAX_LIGHT = 322
NUM_PIXELS = 9


def scale(light_value):
    pixels_to_light = int(light_value / MAX_LIGHT * (NUM_PIXELS))
    if pixels_to_light >= NUM_PIXELS:
        pixels_to_light = NUM_PIXELS
    return pixels_to_light


def blackout():
    for i in range(10):
        cp.pixels[i] = (0, 0, 0)
()


while True:
    light = cp.light
    print((light,))
    time.sleep(0.05)

    pixels_to_light = scale(light)
    for i in range(pixels_to_light):
        cp.pixels[i] = (0, 0, 255)
    for i in range(pixels_to_light, NUM_PIXELS):
        cp.pixels[i] = (0, 0, 0)
    ()

    time.sleep(0.05)


