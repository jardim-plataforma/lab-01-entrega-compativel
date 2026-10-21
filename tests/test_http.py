import json
import threading
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
from http.server import ThreadingHTTPServer
from backend.server import Handler
from consumidores.portal import interpretar as portal
from consumidores.integracao import interpretar as integracao

class HttpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_consumidores_por_http(self):
        with urlopen(self.url + "/api/v1/recursos/svc-001") as response:
            self.assertEqual(response.status, 200)
            payload = json.load(response)
        self.assertIn("ativo", portal(payload))
        self.assertEqual(len(integracao(payload)), 3)

    def test_health(self):
        with urlopen(self.url + "/health") as response:
            self.assertEqual(json.load(response)["status"], "ok")

    def test_frontend_assets(self):
        for path in ("/", "/app.js", "/style.css"):
            with urlopen(self.url + path) as response:
                self.assertEqual(response.status, 200)
                self.assertTrue(response.read())

    def test_rota_desconhecida(self):
        with self.assertRaises(HTTPError) as caught:
            urlopen(self.url + "/rota-inexistente")
        self.assertEqual(caught.exception.code, 404)
