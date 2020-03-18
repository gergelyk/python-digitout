from copy import deepcopy
from digitout import digitout_silent, make_default_config

def test_find_anything():
    uut = object()
    path, match = digitout_silent(uut)
    assert path == 'target'
    assert match['value'] == uut

def test_find_cls_attr():
    sentinel = object()
    class Uut:
        xyz = sentinel
    uut = Uut()

    config = make_default_config()
    config['match']['expression'] = 'lambda value: value == sentinel'
    path, match = digitout_silent(uut, config, locals())

    assert path == "target.xyz"
    assert match['value'] == sentinel

def test_find_obj_attr():
    sentinel = object()
    class Uut:
        def __init__(self):
            self.xyz = sentinel
    uut = Uut()

    config = make_default_config()
    config['match']['expression'] = 'lambda value: value == sentinel'
    path, match = digitout_silent(uut, config, locals())

    assert path == "target.xyz"
    assert match['value'] == sentinel

def test_find_cls_call_attr():
    sentinel = object()
    class Uut:
        def __init__(self):
            self.xyz = sentinel
    uut = Uut

    config = make_default_config()
    config['match']['expression'] = 'lambda value: value == sentinel'
    config['traversal']['call']['skip_classes'] = False

    path, match = digitout_silent(uut, config, locals())

    assert path == "target().xyz"
    assert match['value'] == sentinel

def test_find_iter_item():
    sentinel = object()
    uut = [{'x': 123, 'y': 234}, {'a': sentinel, 'b': 456}]

    config = make_default_config()
    config['match']['expression'] = 'lambda value: value == sentinel'
    path, match = digitout_silent(uut, config, locals())

    assert path == "list(target)[1]['a']"
    assert match['value'] == sentinel

def test_find_iter_key():
    sentinel = object()
    uut = {sentinel: 345, 'b': 456}

    config = make_default_config()
    config['match']['expression'] = 'lambda value: value == sentinel'
    config['traversal']['iter']['inspect'] = False
    config['traversal']['item']['inspect_keys'] = True
    path, match = digitout_silent(uut, config, locals())

    assert path == "list(target.keys())[0]"
    assert match['value'] == sentinel
