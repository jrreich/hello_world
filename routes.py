from flask import Flask, url_for, request, render_template; 
from app import app
import beacon_decode as bcn

#server/Main
@app.route('/')
def index():
    """Renders a sample page."""
    createLink = "<a href = '" + url_for('beacon') + "'>Beacon Decoder</a>"; # url_for usings the function name to point to URL
    return render_template('index3.html')
            #"""<html>
            #    <head>
            #        <title> Jesse's Tools</title>
            #    </head>
            #    <body>
            #        """ + createLink + """
            #    </body>
            #</html>""";

#@app.route('/beacon/<beacon>')
#def beacon_decode(beacon):
#    return 'beacon decoder ' + beacon

@app.route('/beacon', methods=['GET','POST'])
def beacon():
    if request.method == 'GET':
        # Send the user the form
        return render_template('BeaconDecoder3.html')
    elif request.method == 'POST':
        # read beacon ID and save it
        beaconID = request.form['beaconID']        

        #decode and return it
        bcn1 = bcn.beacon(beaconID)
        #return results
        return render_template('BeaconDecoded.html', \
            beaconID = beaconID, \
            beaconID15 = bcn1.bcnID15, \
            countrycode = int(bcn1.country_code,2), \
            protocolcode = bcn1.protocol)

    else: 
        return '<h2> Invalid Request </h2>'

@app.route('/rawburst', methods=['GET','POST'])
def rawburst():
    if request.method == 'GET':
        # Send the user the form
        return render_template('BurstAnalysisForm.html')
    elif request.method == 'POST':
        # read input
        MEOLUT,StartTime = request.form['MEOLUT','StartTime']        

        #find data here

        #return results
        return render_template('BurstAnalysisReturn.html', \
            MEOLUT = MEOLUT, \
            StartTime = StartTime)


    else: 
        return '<h2> Invalid Request </h2>'
@app.route('/create')
def create():
    return ' create page'