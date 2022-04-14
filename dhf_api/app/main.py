import os
from pathlib import Path
import sys
from typing import Dict, Literal, Optional

from pydantic.types import PositiveFloat, PositiveInt
sys.path.append(os.path.abspath("CustomPreprocess.py"))

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
from joblib import dump, load
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import warnings

from .dhf_model import DengueHemorrhagicFeverModelData, HumanPulse, HumanTemperatureFloat
from CustomPreprocess import CustomPreprocess
import __mp_main__
__mp_main__.CustomPreprocess = CustomPreprocess


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

THIS_FOLDER = Path(os.path.abspath(__file__)).parent
model_file = THIS_FOLDER / 'model.joblib'
test_file = THIS_FOLDER / 'testdata.csv'

loaded_rf_model: RandomForestClassifier = joblib.load(model_file)


@app.get("/dhf/test")
def test_predict_dengue_hemorrhagic_fever():
    """
    predict dengue hemorrhagic fever (DHF): TODO
    :param input_json:
    :return: prediction_outcome
    """
    #test data
    data = pd.read_csv(test_file, encoding='utf-8')

    results = loaded_rf_model.predict_proba(data)
    #results = modeltest.test()
    print(results)

    return {"result": results}


@app.post("/dhf")
def predict_dengue_hemorrhagic_fever(
        input_json: DengueHemorrhagicFeverModelData
):
    """
    predict dengue: TODO
    :param input_json:
    :return: prediction_outcome
    """

    print(input_json.json())

    data = input_json.to_data_sequence()

    results = loaded_rf_model.predict_proba(data)

    return {"result": results}

@app.post("/dhf/demo/{id}")
def dhf_demo(
        id: Literal[0, 1, "0", "1"],
        d03_temp_avg: Optional[HumanTemperatureFloat] = None,
        d03_temp_range: Optional[PositiveFloat] = None,
        d03_pulse_rate_avg: Optional[HumanPulse] = None,
        d03_pulse_rate_range: Optional[PositiveInt] = None,
) -> float:
    id = int(id)

    test_data: pd.DataFrame = pd.read_csv(Path("./app/testdata.csv").open())

    prediction_input = test_data.iloc[[id]]

    prediction_input = {
        key: value[id]
        for key, value in prediction_input.to_dict().items()
    }

    prediction_input.update(
        {
            key: value
            for key, value in {
                "d03_temp_avg": d03_temp_avg,
                "d03_temp_range": d03_temp_range,
                "d03_pulse_rate_avg": d03_pulse_rate_avg,
                "d03_pulse_rate_range": d03_pulse_rate_range
            }.items()
            if value is not None
        }
    )

    prediction_input = DengueHemorrhagicFeverModelData.from_flat_dict(prediction_input)

    prediction = loaded_rf_model.predict_proba(prediction_input.to_data_sequence())

    return float(prediction[0][1])
