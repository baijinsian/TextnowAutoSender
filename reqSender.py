import pytextnow ; import http; import threading; import os; import requests
from essential_generators import DocumentGenerator ; from datetime import datetime, timezone, timedelta ; from flask import Flask
#=======================================#
def setInterval(func , time, *arguments):
    e = threading.Event()
    while not e.wait(time):
        func(*arguments)
#=======================================#
Generator = DocumentGenerator()
Format = format
webServer = Flask(__name__)

ESTTime = datetime.now(timezone(timedelta(hours=-4), 'EST'))
client = pytextnow.Client("dev.vecio", sid_cookie="s%3AsQz3eA4g0Bl01148v7juoGha6ud2ZePQ.WrI737vlQXniH5NgjkmDcvtEkiO9VyAthY0Da3kpJXQ", csrf_cookie="s%3AF8t427RI11KaeuGYRSfUUBYq.7HNkqQudB77TNv2II7LLJOAO9u7vOf1sg3wCapqK7q4")
#=======================================#
def sendR():
    try:
        requests.get("https://User1239321.linenporches.repl.co")
    except:
        print("< Failed to send request >")
setInterval(sendR, 10)