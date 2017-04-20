from sys import version_info
import glob, os , pprint ,os.path, re, webbrowser, subprocess,sys,argparse,operator
from itertools import  groupby , dropwhile , chain
from dateutil.parser import parse
from collections import  defaultdict
from datetime import datetime




linpat = "^\\[(\\d+?\\/\\d+?\\/\\d+?\\s\\d+?:\\d+?:\\d+?:\\d+?)\\s\\w+\\]\\s([0-9A-Fa-f]+)\\s=?(\\w+)\\s(\\S)(.*)"
lincomp = re.compile(linpat)

class LData(object):
    """ Produces object that makes up a line"""
    def __init__(self,datime,tid,comp,op,payload):
        self.datime = datime
        self.tid = tid
        self.comp = comp
        self.op = op
        self.payload = payload

def ParseTime(tmpdatime):
        datm = datetime.strptime(tmpdatime, '%m/%d/%y %H:%M:%S:%f')
        return datm
            
def parsetoFields(filename):
        print("opening " + filename)
        with open(filename,'r+') as f:
            tlines = []
            for line in f:
                t = lincomp.search(line)
                if t:
                    #datime = ParseTime(t.group(1))
                    datm = datetime.strptime(t.group(1), '%m/%d/%y %H:%M:%S:%f')
                    print (datm)
                    tid = t.group(2)
                    comp = t.group(3)
                    op = t.group(4)
                    payload = t.group(5)
                    data = LData(datm,tid,comp,op,payload)
                    tlines.append(datm)
                    tlines.append(tid)
                    tlines.append(comp)
                    tlines.append(op)
                    tlines.append(payload)
                    
        return tlines
    
    
def main():
    try:
        response=sys.argv[1]
        print(response)
    except:
        py3 = version_info[0] > 2  
        if py3:
            response = input("Please enter directory where search traces resides;   ")
        else:
            response = raw_input("Please enter directory where search traces resides: ")
    tlines = []
    combolines = []
    for filename in glob.glob(os.path.join(response,'trace*.log')):
        tlines = parsetoFields(filename)
        if tlines:
            combolines.extend(tlines)
            s_comblines = sorted(combolines, key=lambda LData: LData.datetime, reverse=True)
            print "\n".join(s_comblines)
  
        


if __name__ == "__main__":
    main()