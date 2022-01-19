# This modules is about print msg in console to see how is the progress
# of some proccess

import time

# Print iterations progress
def printProgressBar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=100,
    fill="█",
    printEnd="\r",
):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


# import time

# # A List of Items
# items = list(range(0, 57))
# l = len(items)

# # Initial call to print 0% progress
# printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
# for i, item in enumerate(items):
#     # Do stuff...
#     time.sleep(0.1)
#     # Update Progress Bar
#     printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)


def getTime(seconds, hourFlag, minuteFlag, secondFlag) -> str:
    secondStruct_time = time.gmtime(seconds)
    listStruct_time = [
        secondStruct_time.tm_hour,
        secondStruct_time.tm_min,
        secondStruct_time.tm_sec,
    ]
    listFlags = [hourFlag, minuteFlag, secondFlag]
    listConstant = ["hora(s)", "minutos(s)", "segundo(s)"]
    separatorEach = " - "
    separatorBetween = " "
    timeToReturn = ""
    print(listFlags, listConstant, listStruct_time)
    for index, item in enumerate(listFlags):
        separatorEnd = separatorEach if index + 1 < len(listFlags) else ""
        setStruct_timeConstant = (
            str(listStruct_time[index])
            + separatorBetween
            + str(listConstant[index])
            + separatorEnd
        )
        timeToReturn += setStruct_timeConstant if listFlags[index] else ""
        # print(setStruct_timeConstant, timeToReturn)
    return timeToReturn


def report(
    seconds,
    data,
    header=" Reports ",
    char="*",
    cantChar=10,
    msgTime="",
    msgData="",
    hourFlag=True,
    minuteFlag=True,
    secondFlag=True,
):
    headerReady = char * cantChar + header + char * cantChar
    footerReady = (len(header) + 2 * cantChar) * char
    msgTimeReady = msgTime + getTime(seconds, hourFlag, minuteFlag, secondFlag)
    msgTimeData = msgData + str(data)
    bodyReady = msgTimeReady + "\n" + msgTimeData
    print(headerReady)
    print(bodyReady)
    print(footerReady)
    pass
