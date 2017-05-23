def chachastep(motion, posture):

    motion.moveInit()
    motion.wakeUp()
    motion.wbEnable(True)
    posture.goToPosture("StandInit", 0.5)
    footStepsList = [[["LLeg"], [[0.06, 0.1, 0.0]]], [["LLeg"], [[0.00, 0.16, 0.0]]], [["RLeg"], [[0.00, -0.1, 0.0]]],
                     [["LLeg"], [[0.00, 0.16, 0.0]]], [["RLeg"], [[-0.04, -0.1, 0.0]]],
                     [["RLeg"], [[0.00, -0.16, 0.0]]], [["LLeg"], [[0.00, 0.1, 0.0]]], [["RLeg"], [[0.00, -0.16, 0.0]]]]

    stepFrequency = 0.8
    clearExisting = False
    nbStepDance = 2 # defined the number of cycle to make

    for j in range( nbStepDance ):
        for i in range( len(footStepsList) ):
            try:
                motion.setFootStepsWithSpeed(
                    footStepsList[i][0],
                    footStepsList[i][1],
                    [stepFrequency],
                    clearExisting)
            except Exception, errorMsg:
                print str(errorMsg)
                print "This example is not allowed on this robot."
                exit()

    motion.waitUntilMoveIsFinished()
    motion.wbEnable(False)
