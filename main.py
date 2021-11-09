def on_received_number(receivedNumber):
    if receivedNumber == 1:
        basic.show_number(1)
    elif receivedNumber == 2:
        basic.show_number(2)
    elif receivedNumber == 3:
        basic.show_number(3)
    elif receivedNumber == 4:
        basic.show_number(4)
    elif receivedNumber == 5:
        basic.show_number(5)
    else:
        pass
radio.on_received_number(on_received_number)

def doTWO():
    strip.set_matrix_color(3, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 0, neopixel.colors(NeoPixelColors.ORANGE))
def doFOUR():
    strip.set_matrix_color(3, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 0, neopixel.colors(NeoPixelColors.ORANGE))
def doTHREE():
    strip.set_matrix_color(3, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 0, neopixel.colors(NeoPixelColors.ORANGE))
def doFIVE():
    strip.set_matrix_color(3, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 4, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(3, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(1, 0, neopixel.colors(NeoPixelColors.ORANGE))
def doONE():
    strip.set_matrix_color(2, 0, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 2, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 3, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_matrix_color(2, 4, neopixel.colors(NeoPixelColors.ORANGE))
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P13, 8, NeoPixelMode.RGB)
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_TAG_RECOGNITION)
strip.set_matrix_width(5)
strip.set_brightness(30)
radio.set_group(34)

def on_forever():
    pass
basic.forever(on_forever)
