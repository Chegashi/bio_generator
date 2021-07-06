%tensorflow_version 1.x
!pip install -q textgenrnn
from google.colab import files

from datetime import datetime
import os
import sys
from textgenrnn import textgenrnn

model_cfg = {
    'word_level': True,   # set to True if want to train a word-level model (requires more data and smaller max_length)
    'rnn_size': 128,   # number of LSTM cells of each layer (128/256 recommended)
    'rnn_layers': 16,   # number of LSTM layers (>=2 recommended)
    'rnn_bidirectional': False,   # consider text both forwards and backward, can give a training boost
    'max_length': 10,   # number of tokens to consider before predicting the next (20-40 for characters, 5-10 for words recommended)
    'max_words': 20000,   # maximum number of words to model; the rest will be ignored (word-level model only)
}

train_cfg = {
    'line_delimited': False,   # set to True if each text has its own line in the source file
    'num_epochs': 40,   # set higher to train the model for longer
    'gen_epochs': 20,   # generates sample text from model after given number of epochs
    'train_size': 0.8,   # proportion of input data to train on: setting < 1.0 limits model from learning perfectly
    'dropout': 0.0,   # ignore a random proportion of source tokens each epoch, allowing model to generalize better
    'validation': False,   # If train__size < 1.0, test on holdout dataset; will make overall training slower
    'is_csv': False   # set to True if file is a CSV exported from Excel/BigQuery/pandas
}

file_name = "/content/all.txt"
model_name = 'all'   # change to set file name of resulting trained models/texts

textgen = textgenrnn(name=model_name)

train_function = textgen.train_from_file if train_cfg['line_delimited'] else textgen.train_from_largetext_file

train_function(
    file_path=file_name,
    new_model=True,
    num_epochs=train_cfg['num_epochs'],
    gen_epochs=train_cfg['gen_epochs'],
    batch_size=1024,
    train_size=train_cfg['train_size'],
    dropout=train_cfg['dropout'],
    validation=train_cfg['validation'],
    is_csv=train_cfg['is_csv'],
    rnn_layers=model_cfg['rnn_layers'],
    rnn_size=model_cfg['rnn_size'],
    rnn_bidirectional=model_cfg['rnn_bidirectional'],
    max_length=model_cfg['max_length'],
    dim_embeddings=100,
    word_level=model_cfg['word_level'])

files.download('{}_weights.hdf5'.format(model_name))
files.download('{}_vocab.json'.format(model_name))
files.download('{}_config.json'.format(model_name))

textgen = textgenrnn(weights_path='all_weights.hdf5',
                       vocab_path='all_vocab.json',
                       config_path='all_config.json')


original_stdout = sys.stdout
i = 0
with open('all_genn.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    while (i< 500):
        i += 1
        textgen.generate()
        print("$$")
    sys.stdout = original_stdout # Reset the standard output to its original value
files.download('all_gen.txt')
