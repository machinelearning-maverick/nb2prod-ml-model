# nb2prod-ml-model

Core ML model package for `nb2prod`. Contains training and prediction logic.

## Install
```bash
pip install .
```

## Usage
```python
from nb2prod_ml_model import train, predict
model = train.train_model([])
result = predict.predict(model, [])
```
