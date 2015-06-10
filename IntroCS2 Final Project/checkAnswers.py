#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
#import cgitb
#cgitb.enable()

html='<html><head><title>Score</title></head>'

answersPython={1:1,2:2,3:2,4:3,5:1}
answersTerminal={1:1,2:1,3:3,4:3,5:2}
answersHTML={1:3,2:2,3:3,4:1,5:2}
answers={}

q=cgi.FieldStorage()
d={}
for keys in q:
    d[keys]=q[keys].value

if d['quizType']=='Python':
    answers=answersPython
if d['quizType']=='Terminal':
    answers=answersTerminal
if d['quizType']=='HTML':
    answers=answersHTML


def check(d):
    right=0
    pos=1
    improve='<ul>'
    for keys in d:
        if keys=="quizType":
            pos=pos
        elif int(d[keys])==answers[int(keys[0])]:
            right+=1
        else:
            if improve.find(keys[2:])==-1:
                improve=improve+'<li>'+keys[2:]+' </li>'
        pos+=1
    pos-=2
    if right==pos:
        return 'You got '+str(right)+' out of '+str(pos)+' right'
    else:
        return 'You got '+str(right)+' out of '+str(pos)+' right'+'<br><br>Topics that need improvement:'+improve+'</ul>'

html+=check(d)
html+='<br><br>'
html=html+'<a href="'+d['quizType']+'">Answers</a>'
print html