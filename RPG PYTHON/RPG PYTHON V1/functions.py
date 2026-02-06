import time

def underline():
    print("---------------------")

def pause():
    for i in range(2):
        print(".")
        time.sleep(1)

def big_pause():
    for i in range(2):
        print(".")
        time.sleep(2)

def round_end():
    print("Round End ...")
    big_pause()
