# follow.py
#
# Follow a file like tail -f.

# command used: adb shell setconsole > C:\Users\jalerse\Documents\cmdWithPython\output.txt

line_number = 0
list_of_results = []

import time
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

# def searchWord(Word):
#     with open("output.txt") as openfile:
#         for line in openfile:
#             for part in line.split():
#                 if Word in part:
#                     return line
# Word = "onDirective"
list_of_strings = ['Listening', 'Thinking', 'Idle', 'Speaking', 'onDirective']

if __name__ == '__main__':
    logfile = open("output.txt","r")
    loglines = follow(logfile)
    for line in loglines:
        line_number += 1
        for string_to_search in list_of_strings:
            if string_to_search in line:
                list_of_results.append((string_to_search, line_number, line.rstrip()))
                for elem in list_of_results:
                    print(elem[1], ' :: ', elem[2])
        # for part in line.split():
        #     if Word in part:
        #         print (line)