﻿from pxtool.model.util._px_super import _PXSingle
from pxtool.model.util._px_valuetype import _PxInt
from pxtool.model.util._line_validator import LineValidator

class Rounding(_PXSingle): 

    pxvalue_type:str = "_PxInt"
    is_language_dependent:bool = False


    def set(self, rounding:int) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, rounding)
        LineValidator.is_int( self._keyword, rounding)
        LineValidator.in_range(0,1, self._keyword, rounding)
        my_value = _PxInt(rounding)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

