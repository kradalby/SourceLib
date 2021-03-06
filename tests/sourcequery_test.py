import unittest
from SourceLib.SourceQuery import SourceQuery as q

# This server must be up to test, kinda stupid
TEST_SERVER = ('81.166.125.12', 21600)
TEST_SERVER_NAME = 'Hellfragger.no #06 Office Only :: Multigamer.no'
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
