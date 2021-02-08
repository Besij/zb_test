# zb_test

How to run:
  1) Download geko driver for Chrome here:
https://chromedriver.chromium.org/downloads
  2) Install all requirements:
pip install -r requirements.txt
  3) Run tests:
python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*

Remote:
  1) export SELENIUM_HOST=<moon host>
  2) export SELENIUM_PORT=4444
  3) pytest -v --driver Remote --capability browserName chrome tests/*
