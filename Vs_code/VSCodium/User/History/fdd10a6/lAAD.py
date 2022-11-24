import speedtest

test = speedtest.speedtest()

down_speed = test.download()
up_speed = test.upload()

print(f"Download speed: {down_speed}")
print(f"Upload speed: {up_speed}")