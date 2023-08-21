Certainly! Here's the code for the `run.bat` file that allows the user to run `main.py` and install the required dependencies using `pip`:

```batch
@echo off
pip install -r requirements.txt
python main.py
```

To use this `run.bat` file, simply create a new file with a `.bat` extension (for example, `run.bat`), and copy the above code into it. Place the `run.bat` file in the same directory as your `main.py` and `requirements.txt` files. Then, double-click the `run.bat` file to execute it. This will install the required dependencies and then run the `main.py` script.