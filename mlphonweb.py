import sys
import os
from flask import Flask, jsonify, render_template, request
import regex
from mlphon import PhoneticAnalyser

app = Flask(__name__)
# app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template(
        "index.html",
    )


@app.route("/api/syllablize", methods=["GET", "POST"])
def syllablize():
    """Syllablize the input Malayalam string obtained by POST

        Example: കേരളം

    Returns
    -------
    json
        syllables:["കേ","ര", "ളം"]
        0: "കേ"
        1: "ര"
        2: "ളം"
        text:"കേരളം"
    """
    syllablize = {}
    if request.method == "POST":
        text = request.json.get("text")
    else:
        text = request.args.get("text")
    text = text.strip()
    mlphon = PhoneticAnalyser()
    syllables = mlphon.split_to_syllables(text)
    return jsonify({"text": text, "syllables": syllables})


@app.route("/api/g2panalyse", methods=["GET", "POST"])
def g2p_analyse():
    grapheme_analyse = {}
    if request.method == "POST":
        text = request.json.get("text")
    else:
        text = request.args.get("text")
    text = text.strip()
    mlphon = PhoneticAnalyser()
    ipa_and_tags = mlphon.analyse(text)
    # ipa_and_tags = [{'phonemes': [{'ipa': 'k', 'tags': ['plosive', 'voiceless', 'unaspirated', 'velar']}, {'ipa': 'a', 'tags': ['schwa']}]}, {'phonemes': [{'ipa': 'l', 'tags': ['lateral', 'alveolar']}, {'ipa': 'a', 'tags': ['schwa']}]}]
    return jsonify({"text": text, "syllables": ipa_and_tags})


@app.route("/api/getipa", methods=["GET", "POST"])
def getipa():
    getipa = {}
    if request.method == "POST":
        text = request.json.get("text")
    else:
        text = request.args.get("text")
    mlphon = PhoneticAnalyser()
    ipa = mlphon.grapheme_to_phoneme(text)
    return jsonify({"text": text, "IPA": ipa})


@app.route("/api/g2pgenerate", methods=["GET"])
def g2p_generate():
    grapheme_generate = {}
    text = request.args.get("text")
    mlphon = PhoneticAnalyser()
    graphemes = mlphon.phoneme_to_grapheme(text)
    return jsonify({"text": text, "IPA": graphemes})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
