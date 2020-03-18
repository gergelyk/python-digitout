from digitout import digitout_silent, make_default_config

def test_find_ret_val_ann():
    sentinel = object()
    class Uut:
        def xx(self) -> sentinel:
            pass
    uut = Uut()

    config = make_default_config()
    config['match']['expression'] = 'lambda value: value == sentinel'
    path, match = digitout_silent(uut, config, locals())

    assert path == "target.__class__.xx.__annotations__['return']"
    assert match['value'] == sentinel
