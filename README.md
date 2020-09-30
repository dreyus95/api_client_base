## Dependencies

```
pip install -r requirements.txt
```

## Tests

- inside `env/` folder create `test.env` and fill in the blanks from `env/.env`

```
pytest --cov=src -s  # -s captures the output, can be ommited if only success/fail result is interesting
```