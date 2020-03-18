from digitout import digitout_silent, make_default_config

def test_find_item_iter():
    uut = {'a': [123, 234, 345], 'b': [123, 345, 234], 'c': [234, 345, 123]}

    config = make_default_config()
    config['match']['target'] = "iter"
    config['match']['expression'] = "lambda value, index: index > 1 and value == 123"
    path, match = digitout_silent(uut, config)

    assert path == "list(target['c'])[2]"
    assert match['value'] == 123
