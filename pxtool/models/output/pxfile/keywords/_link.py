﻿from pxtool.models.output.pxfile.util._px_super import _PxValueByKey
from pxtool.models.output.pxfile.util._px_valuetype import _PxString
from pxtool.models.output.pxfile.util._px_keytypes import _KeytypeLang
from pxtool.models.output.pxfile.util._line_validator import LineValidator

class _Link(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    has_subkey:bool = False
    subkey_optional:bool = False
    completeness_type:str = "Lang"
    may_have_language:bool = True

    def __init__(self) -> None:
        super().__init__("LINK")
        self._seen_languages={}

    def set(self, link:str, lang:str = None) -> None:
        """ Not in use? """
        LineValidator.is_not_None( self._keyword, link)
        LineValidator.is_string( self._keyword, link)
        my_value = _PxString(link)
        my_key = _KeytypeLang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang]=1

    def get_value(self, lang:str = None) -> str:
        my_key = _KeytypeLang(lang)
        return super().get_value(my_key).get_value()

    def has_value(self, lang:str = None) -> bool:
        my_key = _KeytypeLang(lang)
        return super().has_value(my_key)

    def get_used_languages(self) -> list[str]:
       return list(self._seen_languages.keys())

    def reset_language_none_to(self,lang:str)->None:
        if not lang:
            return
        if None in self.get_used_languages():
             super().reset_language_none_to(lang)
             #unsee None
             del self._seen_languages[None]
             self._seen_languages[lang]=1