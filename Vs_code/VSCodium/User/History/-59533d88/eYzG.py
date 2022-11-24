import speedtest
wifi  = speedtest.speedtest()
print("Wifi Download Speed is ", wifi.download())
print("Wifi Upload Speed is ", wifi.upload())