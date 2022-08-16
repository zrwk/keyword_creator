# Run this script in the same folder as the document you want to turn into a keyword list.
import re


def input_filename():
    """asks user to write the name of the file they want to turn into a keyword list
    it's essential to include the file extension here!"""
    return input("What is the name of the unformatted data (include extension): ")


def read_from_file():
    """Reads data from file into a list, each index is an individual word.
    if this fails, it tells the user to check spelling, and if they added the extension"""
    raw_data = []
    try:
        with open(filename, "r") as f:
            for word in f:
                raw_data += word.split()
        return raw_data
    except:
        print("Unable to open file!")
        print("Please check spelling of file name and ensure extension is included!")


def clean_words(words):
    """This clears up the words and removed any characters not in the whitelist.
    changes all words to lower case, and removed duplicate words"""
    cl = []
    for word in data_from_file:
        cl.append(re.sub(whitelist, "", word).lower())
    cl = set(cl)
    return cl


def write_to_file(keywords):
    # Writes data to new file. Appends prefix "CLEANED - " to filename.
    with open("CLEANED - " + filename, "w") as f:
        for x in keywords:
            f.write(x + "\n")


# whitelist here is characters allowed in each word ----------------------------------------------
# to add new characters, add them inside the () curly brackets -----------------------------------
# Some characters may need to be escaped with "\" ------------------------------------------------
whitelist = r"[^a-zA-Z0-9(\"*$\'\-)]"

# code execution ---------------------------------------------------------------------------------
filename = input_filename()
data_from_file = read_from_file()
cleaned_keywords = clean_words(data_from_file)
write_to_file(cleaned_keywords)
