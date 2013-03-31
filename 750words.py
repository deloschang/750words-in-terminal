# 750 words in the terminal

import thread
import threading

import datetime

# setup the timer
def ask_for_time():
    while True:
        try:
            time = raw_input("how many seconds to write for? ") 

            # catch default response, which is 45 seconds
            if time == '':
                time = 45.0000

            time = int(time)

            break;

        except ValueError:
            pass



    print time,
    print " seconds set! "
    print "\n"

    return int(time)


# start the timer
def set_timer(prompt, timeout=45.0):
    timer = threading.Timer(timeout, thread.interrupt_main)

    # in case user ctrl+c's out
    user_input = None

    try: 
        timer.start()

        user_input = ""

        print prompt

        # ignore newlines, keep concatenating
        while True:
            user_input += "\n"   # add new line first to keep spacing
            user_input += raw_input()

    except KeyboardInterrupt:
        pass

    timer.cancel()
    return user_input


# appends given filename with timestamp
def save_with_time(filename, timestamp="%Y-%m-%d-%H-%M-%S_{filename}"):
    return datetime.datetime.now().strftime(timestamp).format(filename=filename)

# figure out how to prevent Enter from stopping
time = ask_for_time()
response = set_timer("Start typing! :  \n", time)

# save my words
with open("my750/" + save_with_time('750words.txt'), 'w') as my750:
    my750.write(response)


print "\n"
print "Time's up! We saved it for you. You exercised your creativity today!"


