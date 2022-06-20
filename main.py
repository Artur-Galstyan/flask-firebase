import firebase_admin as fb
from firebase_admin import firestore
from flask import Flask
import os
import pathlib


class Firebase:

    def __init__(self, app: Flask, credentials=None, options=None):
        fb.initialize_app(credentials, options)


def main():

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str(pathlib.Path.cwd() / pathlib.Path("service_account.json"))
    firebase_config = {
        "projectId": "firebase-demo-353919",
        "storageBucket": "firebase-demo-353919.appspot.com"
    }

    app = Flask(__name__)
    firebase = Firebase(app, None, firebase_config)
    db = firestore.client()


if __name__ == "__main__":
    main()
