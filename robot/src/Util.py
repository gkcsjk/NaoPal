IP = "192.168.1.100"
PORT = 9559
PI = 3.1415926


# From CSV file to list
def get_music(filepath):
    fo = open(filepath, "r")
    time = []
    for line in fo:
        time.append(float(line))
    return time

# File path of the beats
beats = {
    "sugar": get_music("robot/src/beats/sugar.csv"),
    "free": get_music("robot/src/beats/sugar.csv"),
    "sky": get_music("robot/src/beats/sky.csv"),
    "moon": get_music("robot/src/beats/moon.csv"),
}
# File path of the music
music = {
    "sugar": "/home/nao/naoGUI/sugar.wav",
    "free": "/home/nao/naoGUI/free.wav",
    "sky": "/home/nao/naoGUI/sky.wav",
    "moon": "/home/nao/naoGUI/moon.wav",
}

# File path to store the motion records
PATH = "C:/Users/gkcsj/Desktop"



