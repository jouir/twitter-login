# twitter-login

Grant a Twitter application to use your Twitter account on your behalf.

## Description

If you have a `CONSUMER_KEY` and a `CONSUMER_SECRET`, you would like to have an `ACCESS_TOKEN` and an
`ACCESS_TOKEN_SECRET`, you are at the right place!

## Create consumer tokens

Go to the [developper portal](https://developer.twitter.com/en/portal/dashboard) to create a Twitter application. Go to
"*Keys and tokens*", then "*Consumer keys*" and "*API key & secret*". Those keys are `CONSUMER_KEY` and
`CONSUMER_SECRET` settings.

## Create access tokens

Clone this repository:

```
git clone https://github.com/jouir/twitter-login.git
```

Setup the Python virtual environment:

```
sudo apt install python3-virtualenv
virtualenv venv
source venv/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```

Read consumer keys:

```
read -s CONSUMER_KEY
read -s CONSUMER_SECRET
```

Execute the script:

```
python3 main.py --consumer-key ${CONSUMER_KEY} --consumer-secret ${CONSUMER_SECRET}
```

Open the URL to click on "Authorize app". Go back to the console and write the generated code.

```
Please go to https://api.twitter.com/oauth/authorize?oauth_token=xxxxx
Code: 0000000
Generated tokens:
ACCESS_TOKEN = *****
ACCESS_TOKEN_SECRET = *****
```

Done.

## How to contribute

Please check issues to ensure the feature or bug you are facing is not already known.

Pull requests are highly appreciated.

Ensure to lint the code before submitting a pull-request:

```
docker run -it -v $(pwd):/mnt/ --rm debian:10 bash
apt-get update && apt-get upgrade -y && apt-get install -y python3-pip git
pip3 install pre-commit
cd /mnt
pre-commit run --all-files
```
