# neuralrapper
This is a simple neural net using keras and tensorflow back end to train using a lyrics.txt file (any artist or combination you want).

Upon training, the tool generates lyrics word-by-word.

Quartz did a really nice profile on me and the program here; https://qz.com/920091/a-west-virginia-teen-taught-himself-how-to-build-a-rapping-ai-using-kanye-west-lyrics/

## Setup

Install (with python 2.x--currently working to update code based on python 3.x)

    pip install -U -r requirements.txt 

You may need to add the --user flag at the end.

## Usage

### Data preperation

Guide to using your own lyrics with `lyrics.txt`. The sample lyrics are 3 songs from eminem.

* Avoid including things like "[bridge]" or "[intro]" 

* Seperate each line by a newline

* Avoid non alphanumeric characters (besides basic punctuation)

* You don't have to retype everything - just copy and paste from some lyrics website

### Training

* In `model.py`, change the variable `artist` to the name of the new artist you've used in `lyrics.txt`

* In `model.py`, change the variable `train_mode` to `True`

* Run the program with `python model.py`, and allow training to finish.

### Generating raps

* In `model.py`, if you've trained a new network, the variable `train_mode` will be `True`, set this back to `False`

* Run the program with `python model.py`

* The rap will be written to the output of your terminal, and also to a file called `neural_rap.txt`

### Performing raps

* speech.py will "rap" the generated songs with a text to speech over a generic rap beat (`beat.mp3`), just run `python speech.py`
