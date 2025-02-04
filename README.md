# Bluesky to Pixela Tracker

This repository contains a script that tracks the number of posts you make on [Bluesky](http://bsky.app) each day and logs it to [Pixela](https://pixe.la).

## Prerequisites

Before running the script, ensure you have the following:

- **Python 3** installed
- **Bluesky account**
  - An **App Password** associated with it
- **Pixela account**
  - A **Graph ID** associated with it

## Installation

Run the following commands to set up your environment (only required on first setup):

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Before running the script, configure the required environment variables:

```sh
cp .env.sample .env
```

Then, edit `.env` to provide the appropriate credentials for Bluesky and Pixela.

## Usage

Once everything is set up, run the script with:

```sh
python main.py
```

## Development

To ensure that your changes do not break anything, set up a local **pre-commit hook**:

```sh
mkdir -p .git/hooks
echo "make pre-commit" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

Now, every time you commit, the pre-commit checks will run automatically.
