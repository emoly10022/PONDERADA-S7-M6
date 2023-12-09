import unittest
from historia.historia_services import HistoriaService

class TestHistoriaService(unittest.TestCase):
    def setUp(self):
        self.historia_service = HistoriaService()

    def test_create_historia(self):
        # testa a criação de uma história e a recuperação dessa história do banco de dados
        historia_data = {"content": "Test Content", "id": None}
        created_historia = self.historia_service.create_historia(historia_data)

        # aqui verifica se a história criada é igual a história recuperada do banco de dados
        retrieved_historia = self.historia_service.get_historia_by_id(created_historia.id)
        self.assertIsNotNone(retrieved_historia.id)

    def test_create_historia_from_gpt(self):
        # testa a criação de uma história usando a função historia_gpt e verifica se ela foi salva no banco de dados
        self.historia_service.create_historia_from_gpt()

        # recupera todas as histórias do banco de dados e verifica se pelo menos uma foi criada
        all_historias = self.historia_service.get_all_historias()
        self.assertGreater(len(all_historias), 0)

        # obtém a ultima história criada e verifica se ela possui conteudo e id
        created_historia = all_historias[-1]
        self.assertIsNotNone(created_historia)
        self.assertIsNotNone(created_historia.id)
        self.assertIsNotNone(created_historia.content)

    def test_get_historia_by_id(self):
        # testa a recuperação de uma história específica pelo id após criá-la
        historia_data = {"content": "Test Content", "id": None}
        created_historia = self.historia_service.create_historia(historia_data)

        # recupera a história pelo id e verifica se ela não é nula e possui um id
        retrieved_historia = self.historia_service.get_historia_by_id(created_historia.id)
        self.assertIsNotNone(retrieved_historia)
        self.assertIsNotNone(retrieved_historia.id)

    def test_get_all_historias(self):
        # testa a recuperação de todas as histórias do banco de dados após criar duas histórias
        historia_data_1 = {"content": "Test Content 1", "id": None}
        historia_data_2 = {"content": "Test Content 2", "id": None}

        self.historia_service.create_historia(historia_data_1)
        self.historia_service.create_historia(historia_data_2)

        # recupera todas as histórias e verifica se há pelo menos duas no banco de dados
        all_historias = self.historia_service.get_all_historias()
        self.assertGreater(len(all_historias), 1)

    def test_delete_historia(self):
        # vai testar a exclusão de uma história após criá-la e verifica se ela não pode ser recuperada após a exclusão
        historia_data = {"content": "Test Content", "id": None}
        created_historia = self.historia_service.create_historia(historia_data)

        # exclui a história e verifica se ela não pode ser recuperada
        self.historia_service.delete_historia(created_historia.id)
        deleted_historia = self.historia_service.get_historia_by_id(created_historia.id)
        self.assertIsNone(deleted_historia)

    def test_update_historia(self):
        # testa a atualização do conteúdo de uma história após criá-la e verifica se a atualização foi bem-sucedida
        historia_data = {"content": "Test Content", "id": None}
        created_historia = self.historia_service.create_historia(historia_data)

        # atualiza o conteúdo da história e verifica se a atualização foi bem-sucedidaa
        updated_content = "Updated Content"
        created_historia.content = updated_content
        self.historia_service.update_historia(created_historia.to_json())
        updated_historia = self.historia_service.get_historia_by_id(created_historia.id)
        self.assertEqual(updated_historia.content, updated_content)
