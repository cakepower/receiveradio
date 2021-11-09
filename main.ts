radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        basic.showNumber(1)
    } else if (receivedNumber == 2) {
        basic.showNumber(2)
    } else if (receivedNumber == 3) {
        basic.showNumber(3)
    } else if (receivedNumber == 4) {
        basic.showNumber(4)
    } else if (receivedNumber == 5) {
        basic.showNumber(5)
    } else {
    	
    }
})
radio.setGroup(34)
basic.forever(function () {
	
})
