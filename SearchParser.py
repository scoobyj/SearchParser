from sys import version_info
import glob, os , pprint ,os.path, re, datetime, webbrowser, subprocess,sys,argparse
from itertools import  groupby , dropwhile , chain
from dateutil.parser import parse
from collections import  defaultdict


pat_entry = "(\\[.*?\\])\\s(\\S+)\\s(\\S+)\\s\\S\\s+(PerfLog)\\s(<entry operation)(.*)"
pat_exit = "(\\[.*?\\])\\s(\\S+)\\s(\\S+)\\s\\S\\s+(\\S+)\\s(<exit operation)(.*)"
tentry = re.compile(pat_entry)
texit = re.compile(pat_exit)
pat_t = ("(\\[.*?\\])\\s(\\S+).*?")
thtrc = re.compile(pat_t)


def getfiles(response):
    files = filter(os.path.isfile, glob.glob(os.path.join(response, "trace*.log")))
    files.sort(key=lambda x: os.path.getmtime(x))
    return files
            
      

def groupLinesByMatch(file):
    result = defaultdict(list)

    for line in open(file).readlines():
        matches = thtrc.match(line)
        if matches:    
            result[matches.group(2)].append( line )
    return result.values()


                   
                

def main():
    py3 = version_info[0] > 2  # creates boolean value for test that Python major version > 2
    if py3:
        response = input("Please enter directory where search traces resides;   ")
    else:
        response = raw_input("Please enter directory where search traces resides: ")
    
    files = getfiles(response)
    for file in files:
        #threads = pullThreads(file,response)
        for lines in groupLinesByMatch(file):
            for line in lines:
                tent = tentry.search(line)
                if tent:
                    print ''.join(line)



if __name__ == "__main__":
    main()