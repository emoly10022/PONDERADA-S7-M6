from historia.historia_model import HistoriaModel
from historia.historia_dao import HistoriaDAO
from gpt import historia_gpt

class HistoriaService:
    def __init__(self):
        self.historia_dao = HistoriaDAO()
        
    def create_historia(self, historia_data):
        historia = HistoriaModel(**historia_data)
        self.historia_dao.create_historia(historia)
        return historia
        
    def create_historia_from_gpt(self):
        historia_text = historia_gpt()
        historia_data = {"content": historia_text, "id": None}
        self.historia_dao.create_historia(HistoriaModel(**historia_data))
        
    def get_historia_by_id(self, historia_id):
        return self.historia_dao.get_historia_by_id(historia_id)

    def get_all_historias(self):
        all_historias_data = self.historia_dao.get_all_historias()

        return all_historias_data
    
    def delete_historia(self, historia_id):
        self.historia_dao.delete_historia(historia_id)
        
    def update_historia(self, historia_data):
        historia = HistoriaModel(**historia_data)
        self.historia_dao.update_historia(historia)
        
    def create_historia_from_gpt2(self, historia_data):
        historia_text = historia_gpt()
        historia_data = {"content": historia_text}
        self.historia_dao.create_historia_from_gpt2(HistoriaModel(**historia_data))
        