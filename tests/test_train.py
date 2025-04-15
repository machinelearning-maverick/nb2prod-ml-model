from nb2prod_ml_model import train


def test_train_model():
    result = train.train_model(data=[])
    assert "model" in result
