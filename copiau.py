from flask import Flask, render_template, redirect, url_for



app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('CopiauIndex.html')


@app.route('/expertise')
def services():
    return render_template('CopiauExpertise.html')

@app.route('/services')
def Pricing():
    return render_template('CopiauPricing.html')



if __name__=='__main__':
    app.run(host='0.0.0.0')   

