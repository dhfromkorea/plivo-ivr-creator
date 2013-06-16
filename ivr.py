import os

from flask import Flask, render_template, request, redirect, url_for, session
from flask import Response
import plivo
import requests
import json
import ast


ivr = Flask(__name__)
ivr.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@ivr.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		global ivr_menu
		ivr_menu = ast.literal_eval(request.form['ivr'])
		return redirect(url_for('call'))
	return render_template('enter_json.html')

@ivr.route('/call', methods=['GET', 'POST'])
def call():
	if request.method == 'POST':
		auth_id = "MAMJFLZTGZZGRMMMZMYW"
		auth_token = "NzJlNWEzYWJiOTZiZDk1NTc2ZTJhYjQ3MWI3YzUx"
		p = plivo.RestAPI(auth_id, auth_token)
		number = int(request.form['call'])

		params = {"from": 17322423252, "to": number, "answer_url": "http://agile-tundra-1297.herokuapp.com/answers"}
		response = p.make_call(params)
		
		return Response(json.dumps(response), mimetype='text/json')
	return render_template('call.html')

@ivr.route('/answers', methods=['GET', 'POST'])
def answers():
	
	response = plivo.Response()
	global ivr_menu
	response.addSpeak(body=ivr_menu['message'])
	absolute_action_url = url_for('mm_response', _external=True)
	getDigits = response.addGetDigits(action=absolute_action_url, method='POST',
                                timeout=4, numDigits=1, retries=1)
	return Response(str(response), mimetype='text/xml')

@ivr.route('/main_menu_response', methods=['POST',])
def mm_response():
    post_args = request.form
    global ivr_menu
    input_digit = post_args.get('Digits', None)
    ivr_menu = ivr_menu['actions'][int(input_digit)]
    response = plivo.Response()
    response.addSpeak(input_digit) 
    
    absolute_action_url = url_for('answers', _external=True)
    response.addRedirect(body=absolute_action_url, method='POST')
    return Response(str(response), mimetype='text/xml') 

if __name__ == '__main__':

	ivr.run(debug=True)