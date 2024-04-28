from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# your classes here

class Deck(db.Model):
    """
    Deck Model
    """
    __tablename__ = 'decks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    cards = db.relationship('Card', cascade="delete")
    is_public = db.Column(db.Boolean, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'cards': [card.serialize() for card in self.cards]
        }


class Card(db.Model):
    """
    Card Model
    """
    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'), nullable=False)
    deck = db.relationship('Deck')

    def serialize(self):
        return {
            'id': self.id,
            'deck_id': self.deck_id,
            'question': self.question,
            'answer': self.answer
        }

