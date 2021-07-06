#!bio/bin/python3

from os import system
from bio_app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    
