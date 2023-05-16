from pxtool.model.px_file_model import PXFileModel
from pxtool.model.keywords._language import _Language
from pxtool.operations_on_model.validator.validate_px import Validate
from pxtool.operations_on_model.loaders.loader_pxfile import Loader
from pxtool.operations_on_model.refine.apply_default_language import apply_default_language

import pytest

def test_valdidate_ok():
     big_ok_file = Loader('testdata/statfin_khi_pxt_11xm_full.px')
     big_ok_model = big_ok_file.outModel
     apply_default_language(big_ok_model)
     val = Validate(big_ok_model)
     if not val.is_valid():
          print(val.get_report())

     assert val.is_valid()
     report = val.get_report()
     assert len(val.checks_ran) > 5 

def test_valdidate_exit():
    pxfile = PXFileModel()
    pxfile.languages.set(["sv","fi"])
    
    val = Validate(pxfile)
    assert not val.is_valid
    assert len(val.checks_ran) == 1 
	
    pxfile.language.set("sv")
	
    pxfile.stub.set(["var1_sv","var2_sv"], "sv")
    pxfile.stub.set(["var1_fi","var2_fi"], "fi")

    pxfile.heading.set(["var3_sv"], "sv")
	
    val = Validate(pxfile)
    assert not val.is_valid
    assert len(val.checks_ran) == 2 	
	
    pxfile.heading.set(["var3_fi"], "fi")
    pxfile.contvariable.set("var2_sv","sv")
    val = Validate(pxfile)
    assert not val.is_valid
    assert len(val.checks_ran) == 3 
	
    pxfile.contvariable.set("var2_fi","fi")
    pxfile.values.set(["val1","val2"],"var1_sv","sv")
    pxfile.values.set(["val1","val2","val3","val4_sv"],"var2_sv","sv")
    pxfile.values.set(["val1"],"var3_sv","sv")
    
    pxfile.values.set(["val1","val2"],"var1_fi","fi")
    pxfile.values.set(["val1","val2","val3","val4"],"var2_fi","fi")
	
    pxfile.heading.set(["var3_fi"], "fi")
    pxfile.contvariable.set("var2_sv","sv")
    val = Validate(pxfile)
    assert not val.is_valid
    assert len(val.checks_ran) == 4 
	
    pxfile.values.set(["val1"],"var3_fi","fi")     






