from os import systeme
from bio_app import app
systeme("sed -i '' 's/from keras.backend.tensorflow_backend import set_session/from tensorflow.compat.v1.keras.backend import set_session/g' env/lib/python3.8/site-packages/textgenrnn/textgenrnn.py")
if __name__ == "__main__":
    app.run(debug=True)
    
