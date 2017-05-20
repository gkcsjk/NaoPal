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
}
# File path of the music
music = {
    "sugar": "/home/nao/naoGUI/sugar.wav",
}

# File path to store the motion records
PATH = "C:/Users/gkcsj/Desktop"



