from tic.game_logic import Game_logic
from flo import diff





def test_quitter():
    game=Game_logic()
    diffs = diff(game.play, path="test1.txt")
    assert not diffs, diffs





# def test_bord():
    
#     values = [' ' for x in range(9)]
#     a=print_tic_tac_toe(values)

#     assert expected==a