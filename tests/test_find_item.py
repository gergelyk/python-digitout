from digitout import digitout_silent, make_default_config

def test_find_iter_item():
    uut = [{'a': 123, 'b': 234}, {'a': 345, 'b': 456}]

    config = make_default_config()
    config['match']['target'] = "item"
    config['match']['expression'] = "lambda value, key: key == 'a' and value == 345"
    path, match = digitout_silent(uut, config)

    assert path == "list(target)[1]['a']"
    assert match['value'] == 345
