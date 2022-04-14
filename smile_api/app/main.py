from fastapi import APIRouter, FastAPI
from .smile_model import Model
from .smile_engine import smile
from fastapi.middleware.cors import CORSMiddleware

# dengue_router = APIRouter()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/dengue")
def predict_dengue(input_json: Model):
    """
    predict dengue: TODO
    :param input_json:
    :return: prediction_outcome
    """
    sm = smile.SmileEngine()
    print(input_json.json())
    re = sm.predict(input_json.json())
    return {"result": re}


