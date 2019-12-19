#imports
import tweepy, math, datetime, time

#Tweepy Authorization
f = open("keys.txt", "r")
lines = f.readlines()
consumer_key = str(lines[0]).rstrip("\n")
consumer_secret = str(lines[1]).rstrip("\n")
access_token = str(lines[2]).rstrip("\n)")
access_token_secret = str(lines[3])

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#variables
g = open("date.txt", "r")
lines2 = g.readlines()
sdv_date = int(str(lines2[0]).rstrip("\n"))
sdv_month = int(str(lines2[1]))

#Adjusts the date so that the year stars in spring
def springAdjust(day):
    day2 = day

    if day < 79:
        #before spring
        day2 += 286
    else:
        #after spring
        day2 -= 78
    
    return day2

#Converts Gregorian date to Stardew Valley date
def convertSdDay(day, leap):
    length = 0

    #Adjusts for leap year
    if leap:
        length = 366
    else:
        length = 365
    
    #Conversion
    result = math.ceil((day / length) * 112)

    return result

#Determine the stardew valley seasonal month
def sdSeason(day):
    if day <= 28:
        #Spring
        return 1
    elif day <=56:
        #Summer
        return 2
    elif day <=84:
        #Fall
        return 3
    else:
        #Winter
        return 4

#Returns the day of the month in Stardew Valley Time
def sdDayOfSeason(day, month):
    if month == 1:
        #Spring
        return day
    elif month == 2:
        #Summer
        return day-28
    elif month == 3:
        #Fall
        return day-56
    else:
        #Winter
        return day-84

#Returns the month name from the month number
def seasonString(month):
    if month == 1:
        return "Spring"
    elif month == 2:
        return "Summer"
    elif month == 3:
        return "Fall"
    else:
        return "Winter"

#Finds the day of the week from the stardew valley date
def getDayOfWeek(day):
    if day in (1, 8, 15, 22):
        return "Monday"
    elif day in (2, 9, 16, 23):
        return "Tuesday"
    elif day in (3, 10, 17, 23):
        return "Wednesday"
    elif day in (4, 11, 18, 24):
        return "Thursday"
    elif day in (5, 12, 19, 25):
        return "Friday"
    elif day in (6, 13, 20, 26):
        return "Saturday"
    else:
        return "Sunday"


#Determine if a given year is a leap year
def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year %4 == 0:
        return True
    else:
        return False

#Returns the SDV day of year from current date
def getDayOfYear():
    return convertSdDay(springAdjust(datetime.datetime.utcnow().timetuple().tm_yday), isLeapYear(datetime.datetime.utcnow().year))

#Returns the SDV day of the month from the current date
def getDayOfSeason():
    return sdDayOfSeason(getDayOfYear(), sdSeason(getDayOfYear()))

#Returns the SDV month from the current date
def getMonth():
    return sdSeason(getDayOfYear())

#Returns the SDV season from the current date
def getSeason():
    return seasonString(getMonth())

#Returns the full written out SDV date from the current date
def getFullDate():
    dayOfSeason = getDayOfSeason()
    dayOfWeek = getDayOfWeek(getDayOfSeason())
    season = getSeason()

    return str(dayOfWeek) + ", the " + str(dayOfSeason) + " of " + str(season) + ". "

#Modifiers for special events
def eventModifier(date, month):
    if month == 1:
        if date == 4:
            return "It is Kent's birthday!"
        elif date == 7:
            return "It is Lewis's birthday!"
        elif date == 10:
            return "It is Vincent's birthday!"
        elif date == 13:
            return "The Egg Festival is today!"
        elif date == 14:
            return "It is Haley's birthday!"
        elif date == 15:
            return "Salmonberry Season begins today!"
        elif date == 18:
            return "It is Pam's birthday!"
        elif date == 20:
            return "It is Shane's birthday!"
        elif date == 24:
            return "The Flower Dance is today!"
        elif date == 26:
            return "It is Pierre's birthday!"
        elif date == 27:
            return "It is Emily's birthday!"
        else:
            return ""
    elif month == 2:
        if date == 4:
            return "It is Jas's birthday!"
        elif date == 8:
            return "It is Gus's birthday!"
        elif date == 10:
            return "It is Maru's birthday!"
        elif date == 11:
            return "The Luau is today!"
        elif date == 13:
            return "It is Alex's birthday!"
        elif date == 17:
            return "It is Sam's birthday!"
        elif date == 19:
            return "It is Demetrius's birthday!"
        elif date == 22:
            return "It is The Dwarf's birthday!"
        elif date == 24:
            return "It is Willy's birthday!"
        elif date == 28:
            return "The Dance of the Moonlight Jellies is today!"
        else:
            return ""
    elif month == 3:
        if date == 2:
            return "It is Penny's birthday!"
        elif date == 5:
            return "It is Elliot's birthday!"
        elif date == 8:
            return "Blackberry Season begins today!"
        elif date == 11:
            return "It is Jodi's birthday!"
        elif date == 13:
            return "It is Abigail's birthday!"
        elif date == 15:
            return "It is Sandy's birthday!"
        elif date == 16:
            return "The Stardew Valley fair is today!"
        elif date == 18:
            return "It is Marnie's birthday!"
        elif date == 21:
            return "It is Robin's birthday!"
        elif date == 24:
            return "It is George's birthday!"
        elif date == 27:
            return "Spirit's Eve is today!"
        else:
            return ""
    else:
        if date == 1:
            return "It is Krobus's birthday!"
        elif date == 3:
            return "It is Linus's birthday!"
        elif date == 7:
            return "It is Caroline's birthday!"
        elif date == 8:
            return "The Festival of Ice is today!"
        elif date == 10:
            return "It is Sebastian's birthday!"
        elif date == 14:
            return "It is Harvey's birthday!"
        elif date == 15:
            return "The Night Market begins today!"
        elif date == 17:
            return "It is The Wizard's birthday!"
        elif date == 20:
            return "It is Evelyn's birthday!"
        elif date == 23:
            return "It is Leah's birthday!"
        elif date == 25:
            return "The Feast of the Winter Star is today!"
        elif date == 26:
            return "It is Clint's birthday!"
        else:
            return ""

#Finds seconds until 6 AM EST
def secondsUntilSix():
    tomorrow = datetime.datetime.now() + datetime.timedelta(1)
    six = datetime(year = tomorrow.year, month = tomorrow.month, day = tomorrow.day, hour = 6, minute = 0, second = 0)

    return (six - datetime.datetime.now()).seconds

#Main function
def main():
    tweet = ""
    doTweet = False
    global sdv_date
    global sdv_month
    if sdv_month == getMonth() and sdv_date == getDayOfSeason():
        doTweet = False
    else:
        doTweet = True
    sdv_date = getDayOfSeason()
    sdv_month = getMonth()
    h = open("date.txt", "w")
    h.truncate(0)
    h.writelines([str(sdv_date) + "\n", str(sdv_month)])
    if doTweet:
        tweet = "Today is " + str(getFullDate()) + str(eventModifier(getDayOfSeason(), getMonth()))
        api.update_status(tweet)
main()