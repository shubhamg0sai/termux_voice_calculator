import os
import time
import subprocess
from word2number import w2n
from num2words import num2words

nt1 = "speak You first number"
nt2 = "speak You second number"
op = "speak Your math operator like addition subtraction multiplication division"
r = "the result is"
n = 1

def add():
    subprocess.call(["termux-tts-speak",nt1])
    n1 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n1))
    subprocess.call(["termux-tts-speak",nt2])
    n2 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n2))
    res = w2n.word_to_num(n1) + w2n.word_to_num(n2)
    print(res)
    result = num2words(res)
    print(result)
    subprocess.call(["termux-tts-speak",r,result])


def sub():
    subprocess.call(["termux-tts-speak",nt1])
    n1 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n1))
    subprocess.call(["termux-tts-speak",nt2])
    n2 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n2))
    res = w2n.word_to_num(n1) - w2n.word_to_num(n2)
    print(res)
    result = num2words(res)
    print(result)
    subprocess.call(["termux-tts-speak",r,result])


def mul():
    subprocess.call(["termux-tts-speak",nt1])
    n1 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n1))
    subprocess.call(["termux-tts-speak",nt2])
    n2 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n2))
    res = w2n.word_to_num(n1) * w2n.word_to_num(n2)
    print(res)
    result = num2words(res)
    print(result)
    subprocess.call(["termux-tts-speak",r,result])


def div():
    subprocess.call(["termux-tts-speak",nt1])
    n1 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n1))
    subprocess.call(["termux-tts-speak",nt2])
    n2 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n2))
    res = w2n.word_to_num(n1) / w2n.word_to_num(n2)
    print(res)
    result = num2words(res)
    print(result)
    subprocess.call(["termux-tts-speak",r,result])


def calculator():
    subprocess.call(["termux-tts-speak",op])
    inp = subprocess.getoutput("termux-speech-to-text")
    print("......",str(inp))
    if "addition" in inp:      
        add()
    elif "substraction" in inp:       
        sub()
    elif "multiplication" in inp:      
        mul()
    elif "division" in inp:      
        div()



    else:
        subprocess.call(["termux-tts-speak","wrong operator"])
while n>0:
    calculator()
