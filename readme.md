# Demo the basics of neo-python
First of all I am assuming that you already created your virtual python environment with python3.6 binaries at least. Activate the virtual environment and then execute the command below to install requirements for this project.

`pip install -r requirements.txt`

As next step, we need run docker image for private networks that is provided by neo-python already.

```sh
docker pull cityofzion/neo-privatenet
# This will pull the image then you need to run it by executing the command below
docker run --rm -d --name neo-privatenet -p 20333-20336:20333-20336/tcp -p 30333-30336:30333-30336/tcp cityofzion/neo-privatenet
```

Be patient we are almost there :)
And now it is time to run np-prompt with private net.

`np-prompt -p`

Now we are in the NEO CLI, you can see the state of the blockchain by typing `state`. You should see the results like that:

```sh
neo> state
Progress: 7743 / 20020
Block-cache length 15
Blocks since program start 7743
Time elapsed 1.4815671 mins
Blocks per min 5226.222963509382 
neo> 
```

After a couple mins, progress should be completed. Let's create out brand new wallet

`create wallet tallasWallet`

After you run the command above, ıt will ask you to enter your super secret password twice. (Be sure that you entered at least 10 characters long for the pass.)

After successfull attempts, you wıll see something like this:

```sh
neo> create wallet tallasWallet
[password]> **********
[password again]> **********
[I 180402 21:27:31 UserWallet:197] contract does not exist yet
[I 180402 21:27:31 UserWallet:537] Script hash b'\xe7E"m\xc5\x0fR<\xe7}\xd8+l\xb8\xc5\x82\x13\xe3`\xaf' <class 'bytes'>
Wallet {
    "path": "tallasWallet",
    "addresses": [
        {
            "address": "AcriZMoo4wSC1CqPATHRjGYj8RFMBUpHWQ",
            "script_hash": "e745226dc50f523ce77dd82b6cb8c58213e360af",
            "tokens": null
        }
    ],
    "height": 0,
    "percent_synced": 0,
    "synced_balances": [],
    "public_keys": [
        {
            "Address": "AcriZMoo4wSC1CqPATHRjGYj8RFMBUpHWQ",
            "Public Key": "02345cd4b5bf67366ff34721833dc936189c463ac0c60392b3cfcd3a6ee514e535"
        }
    ],
    "tokens": [],
    "claims": {
        "available": "0.0",
        "unavailable": "0.0"
    }
}
Pubkey b'02345cd4b5bf67366ff34721833dc936189c463ac0c60392b3cfcd3a6ee514e535'
```

Ok take a deep breath and continue on. Now we will switch on **sc-events** config.

`config sc-events on`

Now we will be able to see the events which are happening in background. Let's create a simple **smart contract** for demo purpose.

Here we go! **Yes it is the time.** Now you can run the build command 
```sh
build sc/hello_moto.py test 07 05 True False
```
to build and run `hello_moto.py` script. You should see the all logs in the console.

So all rep is going to [neo-python](https://neo-python.readthedocs.io/en/latest/overview.html) project. You can also find the workshop repo of the neo-python in [here](https://github.com/CityOfZion/python-smart-contract-workshop)

I just created a simple instructions to apply workshop.

**Cya!**