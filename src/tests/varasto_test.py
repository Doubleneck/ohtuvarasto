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

    def test_uudella_varastolla_oikea_tilavuus_kun_init_negatiivinen_tilavuus(self):
        self.varasto = Varasto(-4)
        self.assertAlmostEqual(self.varasto.tilavuus, 0.0)

    def test_uudella_varastolla_oikea_saldo_kun_init_negatiivinen_saldo(self):
        
        self.varasto = Varasto (tilavuus = 10, alku_saldo = -1)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)    

    def test_uudella_varastolla_oikea_alkusaldo(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)    

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

    def test_ottaminen_liikaa_palauttaa_saldon_nolla(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(12)

        self.assertAlmostEqual(self.varasto.saldo, 0.0)     

    def test_ottaminen_liikaa_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(12)

        self.assertAlmostEqual(saatu_maara, 8)

    def test_lisays_liikaa_palauttaa_maksimi_saldon(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, 10)    

    def test_negatiivinen_lisays_liikaa_palauttaa_alkusaldon(self):
        self.varasto.lisaa_varastoon(-4)

        self.assertAlmostEqual(self.varasto.saldo, 0)      

    def test_negatiivinen_ottaminen_tyhjasta_varastosta_palauttaa_alkusaldon(self):
        saatu_maara = self.varasto.ota_varastosta(-4)

        self.assertAlmostEqual(self.varasto.saldo, 0)      

    def test_negatiivinen_ottaminen_palauttaa_saldon(self):
        self.varasto.lisaa_varastoon(4)

        saatu_maara = self.varasto.ota_varastosta(-4)

        self.assertAlmostEqual(self.varasto.saldo, 4) 

    def test_paljonko_mahtuu_palauttaa_oikena_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.tilavuus - self.varasto.saldo
        self.assertAlmostEqual(saatu_maara, 2)     

    def test_ottaminen_str_palauttaa_oikean_printtaukse(self):
        printti = self.varasto.__str__()
        self.assertEqual(printti, 'saldo = 0, vielä tilaa 10')
        

