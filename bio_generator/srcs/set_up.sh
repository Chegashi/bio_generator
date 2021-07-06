apt-get update -y
apt-get update -y
pip install flask
pip install textgenrnn
pip install SQLAlchemy
cp srcs/textgenrnn.py /venv/lib/python3.8/site-packages/textgenrnn/textgenrnn.py


# python3.8 -m venv env
# source env/bin/activate
# env/bin/pip3.8 install -r requirements.txt
# sed -i '' 's/from keras.backend.tensorflow_backend import set_session/from tensorflow.compat.v1.keras.backend import set_session/g' env/lib/python3.8/site-packages/textgenrnn/textgenrnn.pyenv/bin/python3.8 run.py &
# open http://127.0.0.1:5000/