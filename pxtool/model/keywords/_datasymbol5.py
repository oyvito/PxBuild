﻿from pxtool.model.util._px_super import _PXValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _keytype_lang
from pxtool.model.util._line_validator import LineValidator

class Datasymbol5(_PXValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True


    def set(self, datasymbol5:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, datasymbol5)
        LineValidator.is_string( self._keyword, datasymbol5)
        my_value = _PxString(datasymbol5)
        my_key = _keytype_lang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

