#coding=utf-8
import os
import urllib2
import urllib
import time
import json

def writetofile(list_data):
    f = open("1.txt","w")
    for n in list_data:
	print n['utterance']
	f.write(n['utterance'].encode("utf-8"))
    f.close()

def stt_google_wav(filename):
    #Convert to flac
    os.system(FLAC_CONV+ filename+'.wav')
    f = open(filename+'.flac','rb')
    flac_cont = f.read()
    f.close()

    #post it
    lang_code='en_US'
    googl_speech_url = 'https://www.google.com.ua/speech-api/v1/recognize?xjerr=1&client=chromium&pfilter=2&lang=%s&maxresults=6'%(lang_code)
    hrs = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7",'Content-type': 'audio/x-flac; rate=8000'}
    req = urllib2.Request(googl_speech_url, data=flac_cont, headers=hrs)
    p = urllib2.urlopen(req)
    data =  p.read()
    list_data = json.loads(data)["hypotheses"]
    writetofile(list_data)
    return 

FLAC_CONV = 'flac -f ' # We need a WAV to FLAC converter.
if(__name__ == '__main__'):
     stt_google_wav("1")
