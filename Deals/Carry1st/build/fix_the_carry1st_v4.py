# -*- coding: utf-8 -*-
"""One-off (26 Oct 2026): pre-send QA on v4 found 'the Carry1st' (left from 'the Carry1st Shop') on slides 2, 3, 6, 7 and 14. Usage: python3 fix_the_carry1st_v4.py"""
import warnings; warnings.filterwarnings('ignore')
import gs_engine as E
deck = E.Deck('17-dirMLGwFpXBgknXjkvt95rvDW1zNJ7QiaXDvWI8yA')
pairs = [('Launch the Carry1st in', 'Launch Carry1st in'), ('markets, the Carry1st needs', 'markets, Carry1st needs'),
         ('Where the Carry1st sells', 'Where Carry1st sells'), ('between the Carry1st and', 'between Carry1st and'),
         ('run the Carry1st’s payments', 'run Carry1st’s payments')]
deck.run([{'replaceAllText': {'containsText': {'text': a, 'matchCase': True}, 'replaceText': b}} for a, b in pairs], 'the Carry1st -> Carry1st')
print('ok')
