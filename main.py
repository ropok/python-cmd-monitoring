# Print baris dengan keywords yang diinginkan

# command used: adb shell setconsole > output.txt

line_number = 0
list_of_results = []
list_of_keywords = ['']
text_file = "output.txt"

import time
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open(text_file,"r")
    loglines = follow(logfile)
    for line in loglines:
        line_number += 1
        for string_to_search in list_of_keywords:
            if string_to_search in line:
                list_of_results.append((string_to_search, line_number, line.rstrip()))
                for elem in list_of_results:
                    print(elem[1], ' :: ', elem[2])