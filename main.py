import random,time
from playsound import playsound

debugmode=False# if true will print current random number
def rater():
    rate=float(input("enter rate(1-100 higher=slower) : "))
    rate=rate/10
    return rate
try:

    rate=rater()
    while rate>10.0:
        print("Rlly?",rate,"s delay???")
        rate=rater()
    while rate < 0.1:
        print("That's too fast!!",rate,"s delay is very fast!")
        rate=rater()

except:
    print("e")
    rate=1
while True:
    randomuwu=random.randrange(1,100)
    if randomuwu % 5 == 0:
        playsound("sound.mp3")
    if debugmode:
        print(randomuwu)
    time.sleep(rate)
#------------------------------------------------------------------------------#
