# Introduction
This project's objective is to create a conversational agent that carries on a conversation with the user by responding to user’s input with prompts and questions. The role of the conversational agent that we have created is to act as a therapist that specializes in loneliness and being upset. So as you are using this program, try to stay in the mindset of a patient at a therapist’s office to bring out the most of the program's functionality. The conversations you can have has been updated and you can now ask certain questions that are not in the database! The bot can now help if the individual is upset and is struggling with math homework. As Wolfram Alpha is not able to answer a wide range of questions, any question Wolfram Alpha can answer, this bot can now answer as well. The program can now help with Math and Capital City related questions. The program now is also displayed in Korean, therefore a wider range of users can now use this program.

# What's New
In order to improve the chatbot experience, for the Individual Project the following features have been implemented:
| Feature    | Description |
| ---------- | ----------------------------------------------------------------------- |
| Implementing Google Translation | This implentation will translate part of the conversation into another language. This allows the chatbot to be of use by a greater number of people ![Imgur](https://i.imgur.com/OyNxCmQ.png) |
| Implementing the wolframAlpha API| Implementing this API opens up the conversation; however, it is still restricted to what wolframAlpha can answer, you no longer need to only ask questions that are in the database. ![Imgur](https://i.imgur.com/qUP1nmb.png) As you can see, you can ask both questions that are and are not in the database |
| Implementation of the Wikipedia API | This implementation will allow the program to provide a link with more information on the question they are helping the user with. ![Imgur]([Imgur](https://i.imgur.com/5sfIUDr.png))

# How to Run
In order to run the chatbot, you must install NLTK, NLTK Data, and spaCy - Universal Sentence Encoder onto your computer before proceeding.

To install NLTK and NLTK Data, please refer to this link: https://www.nltk.org/install.html

To install spaCy - Universal Sentence Encoder, please refer to this link: https://spacy.io/universe/project/spacy-universal-sentence-encoder or https://github.com/MartinoMensio/spacy-universal-sentence-encoder

As there is a Google Translate API implemented, you will need to install the library needed to run the program, you can do this simply by doing
pip install googletrans into the command line

Due to the implementation of the Wolfram Alpha API you will need to install another library before running. You can simply do this by entering 
pip install wolframalpha into the command line

Once all of these have been installed, clone the Github repository and run the mainGUI class.

- **translateSentence:**
- This is a class with a single function. This class is the Google Translate API that takes in a string a translates the string into Korean. Implemented this by translating parts of the conversation into Korean. 
- **wolframAlpha:**
- This is a class that has a single function. You pass a string through, and using the access key, the string gets passed to Wolfram Alpha and it returns an answer to the question. This function will only get called if the initial question asked is not in the database.
- **WikiSearch:**
- This is a class with a single function that has a single parameter. The function takes in a tag that can be used to search for using the Wikipedia API. It will return a link to the webpage
