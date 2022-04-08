import wolframalpha

class wolframAlpha:
    def wolfram_alpha(question):
        #obtained a private id to be able to access the wolfram API
        wolframPersonalID = 'YA49UX-WY3E47JVAA'
        client = wolframalpha.Client(wolframPersonalID)
        pars = client.query(question)
        answer = next(pars.results).text

        return answer