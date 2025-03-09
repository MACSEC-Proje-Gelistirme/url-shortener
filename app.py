import random
import string
import sqlite3
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
shortenedUrls = {}

def dbConnection():
    conn = sqlite3.connect("urls.db")
    conn.row_factory = sqlite3.Row
    return conn

def initDb():
    conn = dbConnection()
    conn.execute("CREATE TABLE IF NOT EXISTS urls (shortUrl TEXT, url TEXT)")
    conn.commit()
    conn.close()

initDb()




def generateShortUrl(length = 6):
    chars = string.ascii_letters + string.digits
    shortUrl = "".join(random.choice(chars) for _ in range(length))
    return shortUrl

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        shortUrl = generateShortUrl()

        conn = dbConnection()
        while conn.execute("SELECT * FROM urls WHERE shortUrl = ?", (shortUrl,)).fetchone():
            shortUrl = generateShortUrl()

        conn.execute("INSERT INTO urls (shortUrl, url) VALUES (?, ?)", (shortUrl, url))
        conn.commit()
        conn.close()

        return f"Shortened URL: {request.url_root}{shortUrl}"
    
    return render_template("index.html")

@app.route("/<shortUrl>")
def redirectUrl(shortUrl):
    conn = dbConnection()
    row = conn.execute("SELECT * FROM urls WHERE shortUrl = ?", (shortUrl,)).fetchone()
    conn.close()

    if row:
        return redirect(row["url"])
    else:
        return f"Sorry!\nURL for {shortUrl} not found", 404
    
if __name__ == "__main__":
        app.run(debug=True)