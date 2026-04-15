from flask import Flask, render_template, request, redirect
import pandas as pd
import os
import re

app = Flask(__name__)

# Load CSVs
reports = pd.read_csv("reports.csv")
users = pd.read_csv("users.csv")
merged = pd.merge(reports, users, on="USN", how="left")

# Synonym dictionary (same as your terminal version)
synonym_map = {
    "phone": ["mobile", "cellphone", "smartphone", "handset", "android", "cell", "telephone", "device"],
    "iphone": ["apple phone", "ios phone", "smartphone"],
    "wallet": ["purse", "billfold", "money holder", "card holder", "clutch", "coin pouch", "cash holder"],
    # ... keep the rest of your synonyms here
}

def expand_keywords(keyword):
    keywords = [keyword]
    for key, syns in synonym_map.items():
        if keyword.lower() == key or keyword.lower() in syns:
            keywords.append(key)
            keywords.extend(syns)
    return list(set(keywords))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        keyword = request.form["keyword"]
        keywords = expand_keywords(keyword)
        pattern = r'\b(?:' + '|'.join(re.escape(k.lower()) for k in keywords) + r')\b'
        results = merged[
            merged['Description'].str.lower().str.contains(pattern, na=False, regex=True) |
            merged['ItemType'].str.lower().str.contains(pattern, na=False, regex=True)
        ]
        return render_template("results.html", results=results.to_dict(orient="records"))
    return render_template("search.html")

@app.route("/all")
def show_all():
    return render_template("results.html", results=merged.to_dict(orient="records"))

@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        new_row = {
            "Lost/Found": request.form["lost_found"],
            "ItemType": request.form["item_type"],
            "Location": request.form["location"],
            "Time": request.form["time"],
            "Description": request.form["description"],
            "USN": request.form["usn"],
            "ImagePath": request.form["image_path"]
        }
        reports.loc[len(reports)] = new_row
        reports.to_csv("reports.csv", index=False)
        return redirect("/all")
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
