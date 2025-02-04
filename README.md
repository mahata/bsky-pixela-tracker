# What is this repository?

FIXME.

## Prerequisites

* Python3
* [Bluesky](http://bsky.app) Account
  * Also, an App Password associated with it
* [Pixela](978-4-8144-0104-8) Account
  * Also, a Graph ID associated with it

## How to run

The following commands need to be run only for the first time.

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, set up the environment variables as follows:

```
$ cp .env.sample .env
(Fix .env so that the file has appropriate env vars for the service)
```

Finally, run the script:

```
$ python main.py
```
