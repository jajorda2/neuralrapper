# neuralrapper
This is a simple neural net using keras and tensorflow back end to train using a lyrics.txt file (any artist or combination you want).

Upon training, the tool generates lyrics word-by-word.

* I'm calling this      neuralrapper        but it works with any genre really and can even be used with poetry applications (maybe I'll do one with William Blake!)

* Some of the code is based on https://github.com/robbiebarrat/rapping-neural-network from a few years ago, but includes automated lyrics capture and data cleaning methods

## Setup

Install THIS HAS BEEN PORTED TO PYTHON = 3

    sudo apt-get install libhdf5-dev

    pip3 install -r requirements.txt 


## Usage

### Data preperation

Guide to using your own lyrics with `lyrics.txt`.

#### Scraping your own lyrics

* Use NPM (if not installed, see https://tecadmin.net/install-latest-nodejs-npm-on-ubuntu/)

        npm install lyrics-corpus -g

* Fetch Songs (this will fetch 10 songs by eminem in separate txt files):
        
        create-corpus "eminem" 10
        
* Navigate to the newly created directory

        cd eminem
        
* Now we need to combine all the text files into one file. To do this, create a .py (name it anything like "concatenate.py") file in the same directory with the following

        import glob

        read_files = glob.glob("*.txt")

        with open("lyrics.txt", "wb") as outfile:
            for f in read_files:
                with open(f, "rb") as infile:
                    outfile.write(infile.read())

* Execute the concatenate.py file

        python3 concatenate.py

* You should now have a file called "lyrics.txt"

* Copy "lyrics.txt" into the neuralrapper directory

* Avoid including things like "[bridge]" or "[intro]" 

* Seperate each line by a newline

* Avoid non alphanumeric characters (besides basic punctuation)

* There's an included script to do this. See next:

#### Removing stuff from lyrics.txt that causes string errors

* Run 

        python3 nonalpha.py

* The output will be "lyricsclean.txt" which already works with model.py

### Training

* In `model.py`, change the variable `artist` to the name of the new artist you've used in `lyrics.txt`

* In `model.py`, change the variable `train_mode` to `True`

* Run the program with `python3 model.py`, and allow training to finish.

### Generating raps

* In `model.py`, if you've trained a new network, the variable `train_mode` will be `True`, set this back to `False`

* Run the program with `python3 model.py`

* The rap will be written to the output of your terminal, and also to a file called `neural_rap.txt`
