def on_received_number(receivedNumber):
    strip.clear()
    if receivedNumber == 1:
        doONE()
        strip.show()
    elif receivedNumber == 2:
        doTWO()
        strip.show()
    elif receivedNumber == 3:
        doTHREE()
        strip.show()
    elif receivedNumber == 4:
        doFOUR()
        strip.show()
    elif receivedNumber == 5:
        doFIVE()
        strip.show()
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
strip = neopixel.create(DigitalPin.P13, 25, NeoPixelMode.RGB)
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_TAG_RECOGNITION)
strip.set_matrix_width(5)
strip.set_brightness(30)
radio.set_group(34)

def on_forever():
    strip.clear()
    huskylens.request()
    doSomething(huskylens.readBox_s(Content3.ID))
    # strip.rotate(1)
    strip.show()
    basic.pause(500)
basic.forever(on_forever)

def doSomething(num: number):
    if num == 1:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    elif num == 2:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    elif num == 3:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    elif num == 4:
        strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
    elif num == 5:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
    else:
        strip.clear()
