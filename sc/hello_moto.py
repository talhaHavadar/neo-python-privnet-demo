"""
Taken from: https://github.com/CityOfZion/python-smart-contract-workshop/blob/master/2-print-and-notify.py

In prompt.py, you need to execute `config sc-events on` to see the events showing up.
Test & Build:
neo> build sc/hello_moto.py test 07 05 True False
"""
from boa.interop.Neo.Runtime import Log, Notify

def Main():
    # Print translates to a `Log` call, and is best used with simple strings for
    # development info. To print variables such as lists and objects, use `Notify`.
    print("hello moto from default print")
    Log("normal log from Runtime Service")
    Notify("notify from Runtime Service")

    # Sending multiple arguments as notify payload:
    msg = ["a", 1, 2, b"3"]
    Notify(msg)