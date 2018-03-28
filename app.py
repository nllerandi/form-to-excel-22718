from flask import Flask, render_template, request, Response, send_file
import pandas as pd
import numpy as np
import tempfile
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/crm')
def fios():
    return render_template("fios.html")

@app.route('/fiosForm', methods=['POST'])
def fiosForm():
    marketingtactic = request.form["marketingtactic"]
    lineofbusiness = request.form["lineofbusiness"]
    marketingcampaigntype = request.form["marketingcampaigntype"]
    projectcode = request.form["projectcode"]
    landingpageurl = request.form["landingpageurl"]

    # Create a Pandas dataframe from the data.
    df = pd.DataFrame({"Marketing Tactic": [marketingtactic],
                       "Line of Business": [lineofbusiness],
                       "Marketing Campaign Type": [marketingcampaigntype],
                       "Project Code": [projectcode],
                       "Concat": [landingpageurl + "?cmp=" + marketingtactic + "_" + lineofbusiness + "_" + marketingcampaigntype + "_" + projectcode]
                       })

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

    return render_template("downloads.html")

@app.route("/return-file/")
def return_file():
    return send_file("pandas_simple.xlsx", attachment_filename="cmp.xlsx")

if __name__ == '__main__':
    app.run()