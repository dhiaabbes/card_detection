from flask import Flask

app = Flask(__name__)

# Use `app.config.get("ENV")` to check the environment setting safely.
if app.config.get("ENV") == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config.get("ENV") == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

from app import views
