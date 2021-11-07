from tic.game_logic import Game_logic
from flo import diff

def test_the_first():
    game=Game_logic()
    diffs = diff(game.play, path="test1.txt")
    assert not diffs, diffs

def test_second():
    game=Game_logic()
    diffs = diff(game.play, path="to_test.sim.txt")
    assert  not diffs,diffs

def test_therd():
    game=Game_logic()
    diffs = diff(game.play, path="version2.sim.txt")
    assert  not diffs,diffs


