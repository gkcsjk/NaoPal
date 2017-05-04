from naoqi import ALProxy
import Util
import UpperBody

IP = Util.IP
PORT = Util.PORT
LOOP = Util.LOOP
PATH = Util.PATH

motion = ALProxy("ALMotion", IP, PORT)
posture = ALProxy("ALRobotPosture", IP, PORT)
memory = ALProxy("ALMemory", IP, PORT)
battery = ALProxy("ALBattery", IP, PORT)
tts = ALProxy("ALTextToSpeech", IP, PORT)



def print_something(x):
    print x


def rest():
    motion.rest()


def stand():
    motion.setStiffnesses("Body", 1)
    posture.goToPosture("StandInit", 0.5)


def lay():
    motion.setStiffnesses("Body", 1)
    posture.goToPosture("LyingBack", 0.5)


def speak(text):
    tts.say(text)


def walk(x, y, angle):
    motion.setStiffnesses("Body", 1)
    posture.goToPosture("StandInit", 0.5)
    motion.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    motion.post.moveTo(x, y, angle)
    motion.waitUntilMoveIsFinished()


def record(filename):
    motion.setStiffnesses("Body", 1)
    posture.goToPosture("StandInit", 0.5)
    csv_path = UpperBody.record_animation1(motion, memory, PATH, LOOP, filename)
    motion.rest()
    return csv_path


def replay(csv_path):
    motion.setStiffnesses("Body", 1)
    posture.goToPosture("StandInit", 0.5)
    if csv_path != "":
        UpperBody.load_animation(motion, csv_path)


def get_battery():
    value = battery.getBatteryCharge()
    return value


def get_volume():
    return tts.getVolume()


def set_Volume(v):
    tts.setVolume(float(v)/100)
