import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_ei_negatiivinen(self):
        self.assertEqual(Varasto(-1).tilavuus, 0.0)

    def test_alku_saldo_ei_negatiivinen(self):
        self.assertEqual(Varasto(10, -5).saldo, 0.0)

    def test_alku_saldo_ei_yli_tilavuuden(self):
        self.assertEqual(Varasto(10, 15).saldo, 10)

    def test_ei_negatiivista_lisaysta(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisays_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(15)
        self.assertEqual(self.varasto.saldo, 10)

    def test_ei_negatiivista_ottoa(self):
        self.assertEqual(self.varasto.ota_varastosta(-5), 0)

    def test_otetaan_kaikki_mika_voidaan(self):
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(self.varasto.ota_varastosta(10), 5)

    def test_otetaan_kaikki_mika_voidaan_saldon_nollaus(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(10)
        self.assertEqual(self.varasto.saldo, 0)

    def test_oikea_string(self):
        self.assertEqual(str(self.varasto), f"saldo = 0, vielä tilaa 10")

    def test_rikki(self):
        self.assertEqual(self.varasto.saldo, 100)