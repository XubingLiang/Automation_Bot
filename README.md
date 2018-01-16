# Automation_online_study

## please install the newest version of Chrome

## you can set up an virtualenv for it:
```sh
#make the project directory first and head to there
$ virtualenv env
$ . env/bin/activate
```

## follow the instrucstion for main dependencies:
```sh
#install selenium
$ pip install selenium

# provides a nice repl, not needed for selenium
pip install ipython
```

## install chrome driver(you can use brew for macOS)
```sh
$ brew install chromedriver
```
## alternative for installing chromedriver
```sh
#platform options: linux32, linux64, mac64, win32
$PLATFORM=linux64

$VERSION=$(curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE)

$curl http://chromedriver.storage.googleapis.com/$VERSION/chromedriver_$PLATFORM.zip
| bsdtar -xvf - -C env/bin/
```

## check if chrome drive installed
```sh
#you should see the following line after run chromedriver
$ chromedriver
Starting ChromeDriver 2.33.506092 (733a02544d189eeb751fe0d7ddca79a0ee28cce4) on port 9515
Only local connections are allowed.
```
