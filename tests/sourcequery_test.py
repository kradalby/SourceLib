import unittest
from SourceLib.SourceQuery import SourceQuery as q

# This server must be up to test, kinda stupid
TEST_SERVER = ('z.fap.no', 27015)
TEST_SERVER_NAME = 'dfekt.no | Dust2 Only'
TEST_SERVER_GAME = 'Counter-Strike: Source'


class SourceQueryTest(unittest.TestCase):
    def setUp(self):
        self.server = q(TEST_SERVER[0], TEST_SERVER[1])

    def test_name(self):
        self.assertEqual(
            self.server.info()['hostname'],
            TEST_SERVER_NAME
        )

    def test_game(self):
        self.assertEqual(
            self.server.info()['gamedesc'],
            TEST_SERVER_GAME
        )
