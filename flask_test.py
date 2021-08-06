from flask import Flask, request, redirect
import time
app = Flask(__name__)

@app.route("/")
@app.route("/test")
def sms_reply():
	for i in range(100):
		print(i)
		time.sleep(.1)
	return 'Hello world'

if __name__ == '__main__':
	app.debug=True
	app.run(host = '0.0.0.0', port=5000)