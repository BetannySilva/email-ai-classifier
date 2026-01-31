import spacy

# Carrega o modelo de língua portuguesa do spaCy
nlp=spacy.load("pt_core_news_sm")

#Pipeline de normalização textual
def process_email(text:str)->str:
 
    doc = nlp(text.lower())
    
    # Remove stopwords, pontuação e aplica lematização
    tokens =[
        token.lemma_ for token in doc if not token.is_stop and not token.is_punct
    ]
    return " ".join(tokens)