from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import sys
import os
from flask import Flask, jsonify, request, render_template
import requests
import svgwrite


# app = Flask(__PR-Card__)
app = Flask("PR-Card")

# storeに対するCRUD--------------
# GET /store/<string:name>


@app.route('/http', methods=['POST'])
def create_store():
    url = 'https://github-readme-stats.vercel.app/api/top-langs/?username=take-2405'
    response = requests.get(url)
    # dwg = svgwrite.Drawing("Circle.svg")
    # dwg.add(response)
    # dwg.save()

    # dwg = svgwrite.Drawing("Circle.svg")
    # dwg.defs.add(dwg.script(response.content))
    # dwg.save()
    print(response.content)
    # rd_stack = np.concatenate((rd_text, rd_size, rd_font, rd_posi_x1, rd_posi_y1, rd_posi_w1, rd_posi_h1, rd_posi_x2, rd_posi_y2, rd_posi_w2, rd_posi_h2), axis=1)
    # rd_stack
    return "seikou"

# @app.route('/svg' ,methods=['POST'])
# def create_store():
#     args = sys.argv
#     filename = "save.svg"
#     drawing = svg2rlg(filename)
#     renderPM.drawToFile(drawing, "save.png",)
#     return "ok"


@app.route('/')
def home():
    return "aaaa"


app.run(port=8080)
####################
####################
