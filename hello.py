from machine import Timer

tim1 = Timer(0)
tim1.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print('Hello World!'))
