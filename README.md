# PyFirmata Tester

This project contains example programs for pyfirmata

## Installation

Its reccomended that you set up a viruall python envirnmen.

Run the following in the root of the project.

```bash
python3.10 -m venv venv
```

The above will set up a virtual envirnment directory. Next you simply activate it.

```bash
source venv/bin/activate
```

This will activate the virtual envirnment. Now all thats left is to install the dependencies

```bash
python -m pip install -r requirements.txt
```

## Testing our first program

With the virtual env activated we can now run our led script.

Note: you must first find the port the arudino is connected too.

```bash
python led.py
```

If configured corectly the led on the arduino will start to blink.

## Finding Port

In order to find the port on a mac simply run the command

```bash
ls /dev/tty.*
```
