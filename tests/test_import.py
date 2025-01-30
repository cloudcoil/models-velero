from types import ModuleType

import cloudcoil.models.velero as velero


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), velero.__dict__.values()))
    assert modules, "No modules found in velero"
