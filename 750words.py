# 750 words in the terminal
import thread
import threading

import datetime

# setup the timer
def ask_for_time():
    time = raw_input("how long to write for?") 

    # catch default response, which is 45 seconds
    if time == '':
        time = 45.0000

    print "    " +  str(time) + "45 seconds set.    "

    return time


# start the timer
def set_timer(prompt, timeout=45.0):
    timer = threading.Timer(timeout, thread.interrupt_main)

    # in case user ctrl+c's out
    user_input = None

    try: 
        timer.start()
        user_input = raw_input(prompt)
    except KeyboardInterrupt:
        pass
    timer.cancel()
    return user_input




time = ask_for_time()
response = set_timer("Start typing! :  \n", time)

# save the response
print response


