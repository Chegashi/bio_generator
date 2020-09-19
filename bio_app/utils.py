import sys
from textgenrnn import textgenrnn
import random
from bio_app.models import Content, init_db
from io import StringIO


# from bio_app.models import
def gen_bio(domaine='all', created_by='machine', build=False):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    if(build):
        textgen = textgenrnn(weights_path='bio_app/textgen/trainig/{}_weights.hdf5'.format(domaine), 
                            vocab_path='bio_app/textgen/trainig/{}_vocab.json'.format(domaine),
                            config_path='bio_app/textgen/trainig/{}_config.json'.format(domaine))
        textgen.generate()
    else:
        if (domaine == 'all' and created_by == 'human'):
            domaine_list = ["data", "desing", "devlepement", "economie", "security"]
            contents = Content.query.filter(Content.domaine == domaine_list[random.randrange(0, 5)] and Content.created_by== 'human').all()
        contents = Content.query.filter(Content.domaine == domaine and Content.created_by== created_by).all()
        print((random.choice(contents)).summery)    
    s= mystdout.getvalue()
    sys.stdout = old_stdout
    return s
