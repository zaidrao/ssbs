import platform
b = platform.architecture()[0]
if b == '64bit':
    import SSB
elif b == '32bit':
    print("NOT SUPPORTED")