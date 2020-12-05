#! /usr/bin/python
# -*- coding:utf-8 -*-

###################################################################
#                                                                 #
#                            	Config		                      #
#                                                                 #
###################################################################

from flask import Flask, request, render_template, Response
from datetime import datetime

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

###################################################################
#                                                                 #
#                         Html Templates                          #
#                                                                 #
###################################################################

@app.route('/', methods=['GET'])
def index():
	d = datetime.now().strftime("%d/%m/%Y")
	h = datetime.now().strftime("%H")
	m = datetime.now().strftime("%M")
	s = datetime.now().strftime("%S")
	return render_template('index.html', titre="Accueil - E-Space", date=d, hour=h, min=m, sec=s)

@app.route('/galaxy', methods=['GET'])
def galaxy():
	d = datetime.now().strftime("%d/%m/%Y")
	h = datetime.now().strftime("%H")
	m = datetime.now().strftime("%M")
	s = datetime.now().strftime("%S")
	return render_template('galaxy.html', titre="Galaxies - E-Space", date=d, hour=h, min=m, sec=s)

@app.route('/system', methods=['GET'])
def system():
	d = datetime.now().strftime("%d/%m/%Y")
	h = datetime.now().strftime("%H")
	m = datetime.now().strftime("%M")
	s = datetime.now().strftime("%S")
	return render_template('system.html', titre="Systèmes - E-Space", date=d, hour=h, min=m, sec=s)

@app.route('/contact', methods=['GET'])
def contact():
	d = datetime.now().strftime("%d/%m/%Y")
	h = datetime.now().strftime("%H")
	m = datetime.now().strftime("%M")
	s = datetime.now().strftime("%S")
	return render_template('contact.html', titre="Contact - E-Space", date=d, hour=h, min=m, sec=s)

@app.route('/redirect', methods=['POST'])
def redirect():
	d = datetime.now().strftime("%d/%m/%Y")
	h = datetime.now().strftime("%H")
	m = datetime.now().strftime("%M")
	s = datetime.now().strftime("%S")
	return render_template('redirect.html', titre="Redirection - E-Space", date=d, hour=h, min=m, sec=s)

@app.route('/admin', methods=['GET'])
def admin():
	return ('<h1>Error 401 : Unauthorized</h1>')

###################################################################
#                                                                 #
#                       Html Dark Templates                       #
#                                                                 #
###################################################################

@app.route('/dark', methods=['GET'])
def dark_index():
	d = datetime.now().strftime("%d/%m/%Y")
	h = datetime.now().strftime("%H")
	m = datetime.now().strftime("%M")
	s = datetime.now().strftime("%S")
	return render_template('dark_index.html', titre="Accueil - E-Space", date=d, hour=h, min=m, sec=s)

@app.route('/dark/galaxy', methods=['GET'])
def dark_galaxy():
	d = datetime.now().strftime("%d/%m/%Y")
	h = datetime.now().strftime("%H")
	m = datetime.now().strftime("%M")
	s = datetime.now().strftime("%S")
	return render_template('dark_galaxy.html', titre="Galaxies - E-Space", date=d, hour=h, min=m, sec=s)

@app.route('/dark/system', methods=['GET'])
def dark_system():
	d = datetime.now().strftime("%d/%m/%Y")
	h = datetime.now().strftime("%H")
	m = datetime.now().strftime("%M")
	s = datetime.now().strftime("%S")
	return render_template('dark_system.html', titre="Systèmes - E-Space", date=d, hour=h, min=m, sec=s)

@app.route('/dark/contact', methods=['GET'])
def dark_contact():
	d = datetime.now().strftime("%d/%m/%Y")
	h = datetime.now().strftime("%H")
	m = datetime.now().strftime("%M")
	s = datetime.now().strftime("%S")
	return render_template('dark_contact.html', titre="Contact - E-Space", date=d, hour=h, min=m, sec=s)

@app.route('/dark/redirect', methods=['POST'])
def dark_redirect():
	d = datetime.now().strftime("%d/%m/%Y")
	h = datetime.now().strftime("%H")
	m = datetime.now().strftime("%M")
	s = datetime.now().strftime("%S")
	return render_template('dark_redirect.html', titre="Redirect - E-Space", date=d, hour=h, min=m, sec=s)

###################################################################
#                                                                 #
#                             Main                                #
#                                                                 #
###################################################################

if __name__ == '__main__':
	app.run(host= '0.0.0.0', debug=True, port=5000)