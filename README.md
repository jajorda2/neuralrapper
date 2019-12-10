# neuralrapper
This is a simple neural net using keras and tensorflow back end to train using a lyrics.txt file (any artist or combination you want).

Upon training, the tool generates lyrics word-by-word.

## Setup

Install (with python 2.x--currently working to update code based on python 3.x)

    pip install -U -r requirements.txt 

You may need to add the --user flag at the end.

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

        python concatenate.py

* You should now have a file called "lyrics.txt"

* Copy "lyrics.txt" into the neuralrapper directory

* Avoid including things like "[bridge]" or "[intro]" 

* Seperate each line by a newline

* Avoid non alphanumeric characters (besides basic punctuation)

* There's an included script to do this. See next:

#### Removing stuff from lyrics.txt that causes string errors

* Run 

        python nonalpha.py

* The output will be "lyricsclean.txt" which already works with model.py

### Training

* In `model.py`, change the variable `artist` to the name of the new artist you've used in `lyrics.txt`

* In `model.py`, change the variable `train_mode` to `True`

* Run the program with `python model.py`, and allow training to finish.

### Generating raps

* In `model.py`, if you've trained a new network, the variable `train_mode` will be `True`, set this back to `False`

* Run the program with `python model.py`

* The rap will be written to the output of your terminal, and also to a file called `neural_rap.txt`
