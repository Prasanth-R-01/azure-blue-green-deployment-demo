from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "Blue")
    version = os.getenv("APP_VERSION", "1.0")
    release_status = os.getenv("RELEASE_STATUS", "Stable")
    deploy_time = os.getenv(
        "DEPLOY_TIME",
        datetime.utcnow().strftime("%d %b %Y %H:%M UTC")
    )

    return render_template(
        "index.html",
        environment=environment,
        version=version,
        release_status=release_status,
        deploy_time=deploy_time
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
