from flask import Flask, render_template, request, Response, send_file
import pandas as pd
import numpy as np
import tempfile
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fios')
def fios():
    return render_template("fios.html")

@app.route('/fiosForm', methods=['POST'])
def fiosForm():
    note = request.form["note"]
    marketingtactic = request.form["marketingtactic"]
    lineofbusiness = request.form["lineofbusiness"]
    marketingcampaigntype = request.form["marketingcampaigntype"]
    projectcode = request.form["projectcode"]
    marketinggroup = request.form["marketinggroup"]
    inmarketdate = request.form["inmarketdate"]
    platform = request.form["platform"]
    description = request.form["description"]
    misc = request.form["misc"]
    landingpageurl = request.form["landingpageurl"]
    encodedurl = landingpageurl + "?cmp=" + marketingtactic + "_" + lineofbusiness + "_" + marketingcampaigntype + "_" + projectcode + "_" + marketinggroup + "_" + inmarketdate + "_" + platform + "_" + projectcode + "_" + description + "_" + misc

    note2 = request.form["note2"]
    marketingtactic2 = request.form["marketingtactic2"]
    lineofbusiness2 = request.form["lineofbusiness2"]
    marketingcampaigntype2 = request.form["marketingcampaigntype2"]
    projectcode2 = request.form["projectcode2"]
    marketinggroup2 = request.form["marketinggroup2"]
    inmarketdate2 = request.form["inmarketdate2"]
    platform2 = request.form["platform2"]
    description2 = request.form["description2"]
    misc2 = request.form["misc2"]
    landingpageurl2 = request.form["landingpageurl2"]
    encodedurl2 = landingpageurl2 + "?cmp=" + marketingtactic2 + "_" + lineofbusiness2 + "_" + marketingcampaigntype2 + "_" + projectcode2 + "_" + marketinggroup2 + "_" + inmarketdate2 + "_" + platform2 + "_" + projectcode2 + "_" + description2 + "_" + misc2

    d = {
        "Note": [note, note2],
        "Encoded_URL": [encodedurl, encodedurl2]
         }

    df = pd.DataFrame(d, columns = ["Note", "Encoded_URL"])

    # Create a Pandas dataframe from the data.
    # df = pd.DataFrame({"Note": [note],
    #                    "Marketing Tactic": [marketingtactic],
    #                    "Line of Business": [lineofbusiness],
    #                    "Marketing Campaign Type": [marketingcampaigntype],
    #                    "Project Code": [projectcode],
    #                    "Marketing Group": [marketinggroup],
    #                    "In Market Date": [inmarketdate],
    #                    "Platform": [platform],
    #                    "Description": [description],
    #                    "Misc": [misc],
    #                    "Encoded URL": [landingpageurl + "?cmp=" + marketingtactic + "_" + lineofbusiness + "_" + marketingcampaigntype + "_" + projectcode + "_" + marketinggroup + "_" + inmarketdate + "_" + platform + "_" + projectcode + "_" + description + "_" + misc]
    #                    })

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