# Flash Card

A GUI Application to help you recall word meanings from one language to another.

## Description
The application is designed to practice if you remember the meaning of words from a new language you are learning to a familiar language. Here, I have used French as a newly learnt language and English as the familiar language. You can make your own csv file with your preferred languages and words using Google Sheets.

The application shows a flash card with a French word for 3 seconds and then flashes the English meaning of the word automatically. You are supposed to recall meaning of the French word in your head within that period. If you knew the correct meaning, press the tick marked button or else the cross marked button. The words you marked known won't appear again on the flash card.

### Functionality
A new csv file is created "words_to_lear.csv" and a dataframe is created from it using [pandas](https://pandas.pydata.org/docs/index.html)\
(Note - \
The new file is only created when you mark a word as known. So, to avoid FileNotFoundError try, except, else statements are used.)\
Using Tkinter module, an application interface is created with given description.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pandas.

```bash
pip install pandas
```

## Usage

```python
# import statements
import pandas as pd
import tkinter
import random

# reads csv file and creates a dataframe
data = pd.read_csv('xyz.csv')

# returns a random item from a list
a = random.choice(list_name)

# creates button object in a window object
window = tkinter.Tk()
button = tkinter.Button(command=func_name)

#lets tkinter run the application the window
window.mainloop()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
