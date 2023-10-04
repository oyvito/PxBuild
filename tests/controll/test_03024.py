import pytest
import pxtool
from pxtool.models.output.pxfile.px_file_model import PXFileModel
import testdata.expected.test_data_03024 as expected

@pytest.fixture()
def out_model():
    data_loader = pxtool.LoadFromPxmetadata('03024', 'example_data/pxtoolconfig/ssb_config.json')
    return data_loader._out_model

def test_03024_data(out_model:PXFileModel) -> None:
    actual_data = out_model.data.get_value()

    assert actual_data == expected.DATA

def test_03024_decimals(out_model:PXFileModel) -> None:
    actual_decimals = out_model.decimals.get_value()

    assert actual_decimals == expected.DECIMALS

    


    