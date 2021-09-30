
def formatDuration(seconds : int):

    datetime_hour = round(seconds / (60 * 60))
    minute = round(seconds / 60)
    second = round(seconds % 60)

    if int(datetime_hour) <= 0:
        return "{0}:{1}".format(minute, second)
    else:
        return "{0}:{1}:{2}".format(datetime_hour, minute, second)