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
aup = ALProxy("ALAudioPlayer", IP, PORT)


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


def record(filename, type):
    motion.setStiffnesses("Body", 1)
    posture.goToPosture("StandInit", 0.5)
    if type == 'torque':
        csv_path = UpperBody.record_animation(motion, memory, PATH, LOOP, filename)
    elif type == 'free':
        csv_path = UpperBody.record_animation1(motion, memory, PATH, LOOP, filename)
    else:
        csv_path = UpperBody.record_animation_buttons(motion, memory, PATH, filename)
    motion.rest()
    return csv_path


def replay(csv_path):
    motion.setStiffnesses("Body", 1)
    posture.goToPosture("StandInit", 0.5)
    if csv_path != "":
        UpperBody.load_animation(motion, csv_path)


def replay_music(csv_path, beats):
    motion.setStiffnesses("Body", 1)
    posture.goToPosture("StandInit", 0.5)
    if csv_path != "":
        beats_list = Util.beats[beats]
        aup.post.playFile(Util.music[beats])
        UpperBody.load_animation_with_beats(motion, beats_list, csv_path)


def get_battery():
    value = battery.getBatteryCharge()
    return value


def get_volume():
    return tts.getVolume()


def set_Volume(v):
    tts.setVolume(float(v)/100)
