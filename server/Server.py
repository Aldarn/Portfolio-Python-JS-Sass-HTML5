# Flask imports
from flask import Flask, request, redirect, url_for

import traceback
import common

class Server (object):
    """
    Manages the Flask server and related processes.
    """

    FLASK_APP       = Flask(__name__)
    FLASK_APP.debug = True

    def __init__ (self, host = common.FLASK_HOST, port = common.FLASK_PORT):
        """
        Creates the flask server.
        """
        # Save the parameters
        self.host               = host
        self.port               = port

        # Start the Flask server
        http                    = WSGIServer((host, port), self.FLASK_APP)
        http.serve_forever()


    # Index page
    @FLASK_APP.route("/")
    def index ():
        """
        Placeholder.
        
        TODO: Do something with this...
        """
        return "Hello World!"
