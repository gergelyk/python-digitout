from digitout import digitout_silent, make_default_config

def test_find_iter_item():

    class Foo:

        x = 123
        y = 234
        z = 345

        class Bar:

            x = 345
            y = 123
            z = 234

        class Baz:

            x = 345
            y = 234
            z = 123

    uut = Foo

    config = make_default_config()
    config['match']['target'] = "attr"
    config['match']['expression'] = "lambda value, name: name == 'z' and value == 123"
    path, match = digitout_silent(uut, config)

    assert path == "target.Baz.z"
    assert match['value'] == 123
