mycondition = None
limit = 0


def setvalue():
    global mycondition

    mycondition = "yes"

def getvalue():

    return mycondition

def clearvalue():
    global mycondition

    mycondition = None


def setlimit():
    global limit

    limit = 1

def getlimit():
    return limit

def clearlimit():
    global limit

    limit = 0