import pytest

class TestSaludos:
    def test_saludo(self):
        assert "hola" == "hola", "Saludo no exitoso!"

#  este no lo ejecutara
    @pytest.mark.skip(reason="Saltamos la prueba (test_saludo2) porque no la entiendo")
    def test_saludo2(self):
        assert "hola" == "hola", "Saludo2 no exitoso!"
