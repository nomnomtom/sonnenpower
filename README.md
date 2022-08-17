# Sonnenpower Sumup Service

By Tom Dierenfeld for the role of Senior Python Backend Developer @ sonnen GmbH, 2022-08-17

* [tom@hobbitshop24.biz](mailto:tom@hobbitshop24.biz)
* [linkedin.com/tom-dierenfeld](https://www.linkedin.com/in/tom-dierenfeld/)

## Running sonnenpower

### From the command line
This assumes a POSIX style command line. The file accepts exactly one argument, which can be given like this:

```commandline
python3 main.py "$(cat <<'EOF'
{
    "data": {
        "attributes": {
            "list": [
                {
                    "power": "12",
                    "date": "2019-01-22"
                },
                {
                    "value": "8",
                    "date": "2019-02-22"
                }
            ]
        }
    }
}
EOF
)"
```

### From ipython

```python
In [1]: from main import main

In [2]: params1 = {
   ...:     "data": {
   ...:         "attributes": {
   ...:             "list": [
   ...:                 {
   ...:                     "power": "12",
   ...:                     "date": "2019-01-22"
   ...:                 },
   ...:                 {
   ...:                     "value": "8",
   ...:                     "date": "2019-02-22"
   ...:                 }
   ...:             ]
   ...:         }
   ...:     }
   ...: }
   ...: 
   ...: params2 = {
   ...:     "data": {
   ...:         "attributes": {
   ...:             "list": [
   ...:                 {
   ...:                     "power": "6",
   ...:                     "date": "2019-01-22"
   ...:                 }
   ...:             ]
   ...:         }
   ...:     }
   ...: }

In [3]: main(params2)
Out[3]: {'data': {'attributes': {'result': {'value': '0.5062'}}}}

```

## Running Tests

From the command line, run `pytest test_main.py`, if you are in the same directory, `pytest` without further arguments should suffice as well.