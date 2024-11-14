import main


def test_result():
    bank = main.BankInterest(100000, 3, 10)
    assert len(bank.ann_int()) == 2
    assert bank.ann_int() == (3226.72, 1161610.87)
