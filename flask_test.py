from flask import Flask, request, redirect
import time
import os
app = Flask(__name__)

@app.route("/")
@app.route("/test")
def sms_reply():
	for i in range(100):
		print(i)
		time.sleep(.1)

	print('current time is:')
	print(time.ctime())

	print('working dir is')
	c= os.getcwd()
	print(c)
	print(os.listdir(c))

	with open('myster.txt','w') as f:
		f.write('hi friends')
	return 'Hello world'

if __name__ == '__main__':
	app.run()