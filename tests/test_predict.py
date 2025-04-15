from nb2prod_ml_model import predict


def test_predict():
    result = predict.predict({}, input_data=[])
    assert "result" in result
