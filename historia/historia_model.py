        
class HistoriaModel:
    def __init__(self, content, id):
        self.content = content
        self.id = id

    def to_json(self):
        return {
            'id': self.id,
            'content': self.content
        }
