import spacy

nlp=spacy.load("pt_core_news_sm")

#Pipeline de normalização textual
def process_email(text:str)->str:
 
    doc = nlp(text.lower())
    tokens =[
        token.lemma_ for token in doc if not token.is_stop and not token.is_punct
    ]
    return " ".join(tokens)