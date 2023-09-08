﻿import pytest
from pxtool.model.keywords._title import _Title
    
def test_Title_set_valid():
    obj = _Title()
    assert not obj.has_value("no")    
    obj.set("a string","no")
    assert obj.has_value("no")    
    assert obj.get_value("no") == "a string"
    
def test_Title_used_languages():
    obj = _Title()
    obj.set("a string","no")
    assert "no" in obj.get_used_languages()

def test_Title_reset_language():
    obj = _Title()
    obj.set("a string",)
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Title_duplicate_set_raises():
    obj = _Title()
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")