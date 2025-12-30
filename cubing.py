from random import choice
from time import sleep
import os


random_lyrics = [
    "Grab one down, turn it around,",
    "Cross goes down, F2L all around,",
    "OLL looks rough, PLL’s enough,",
    "Finger tricks fly, sub-ten goes by,",
    "Pop on the turn? Lube it, return,",
    "Last scramble’s set, PB threat,",
    "Timer is ready, hands are steady,"
]

verse1 = lambda num: f"{num} speed cubes to solve on the mat,"
verse2 = lambda num: f"{num} speed cubes to solve!"
verse3 = lambda: choice(random_lyrics)
verse4 = lambda num: f"{num} speed cubes to solve on the mat!"


count = 99
sleep_seconds = 1

while count > 0:
    print(verse1(count))
    sleep(sleep_seconds)
    print(verse2(count))
    sleep(sleep_seconds)
    print(verse3())
    sleep(sleep_seconds)
    count -= 1
    print(verse4(count))
    sleep(sleep_seconds)
    os.system('cls')

