# # bio_generator
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://twitter.com/chegashi)  [![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](https://twitter.com/Jihad_Zahir)

Bio generator for Junior Data Scientists, designer, developer, economist and Cybersecurity Analyst. A tool that automatically generates biographies
,as a project at the Cadi Ayyad University, by computer science department under the guidance of Professor :Jihad Zahir

![exepr](/bio_app/static/img/screen.png)

## Pour commencer

Python,  Tensorflow/keras, Flask
### Pré-requis

python3 

### Installation

```sh
git clone https://github.com/Chegashi/bio_generator
cd bio_generator
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
``` 

## Démarrage

```sh
python3.8 run.py 
```
got to http://127.0.0.1:5000/


[datasets](https://github.com/Chegashi/bio_generator/tree/master/bio_app/textgen/datasets)
[text generated](https://github.com/Chegashi/bio_generator/tree/master/bio_app/textgen/output)
[train scripte ](https://github.com/Chegashi/bio_generator/blob/master/bio_app/textgen/trainig/train.py)

## N.B


if you have an ereur in textgenrnn module  "env/lib/python3.8/site-packages/textgenrnn/textgenrnn.py"  replace line number 14 with 
 <br /> "from tensorflow.compat.v1.keras.backend import set_session"

![Étapes]("/bio_app/static/img/Étapes de la réalisation du projet.png")

![structure](/bio_app/static/img/structure_app.png)

![user_exepr](/bio_app/static/img/user_exepr.png)

## Made with


* [Octoparse](https://www.octoparse.com/) -Web Scraping Tool. Automate Data Extraction from websites within clicks without coding.
* [TwitHelper ](https://business.twitter.com/fr/help/campaign-measurement-and-analytics/pixel-helper.html) - chrome extention using to Scraping data from twiter
* [vscode](https://code.visualstudio.com/) - source-code editor.

## Ressources

* [textgenrnn](https://github.com/minimaxir/textgenrnn)
* [stackabuse](https://stackabuse.com/text-generation-with-python-and-tensorflow-keras/)
* [openclassrooms](https://openclassrooms.com/fr/courses/4425066-concevez-un-site-avec-flask)
* [w3schools](https://www.w3schools.com/)
* [MIT](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-864-advanced-natural-language-processing-fall-2005/)

