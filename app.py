from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Tarun Saroch"
    try:
        username = os.getlogin()
    except Exception:
        username = os.environ.get("USER", "unknown")

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"], universal_newlines=True)
    except Exception as e:
        top_output = str(e)
    
    html_output = f"""
    <html>
      <head>
        <title>HTOP Info</title>
      </head>
      <body>
        <h1>Server Info</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time in IST:</strong> {server_time}</p>
        <pre>{top_output}</pre>
      </body>
    </html>
    """
    return html_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
