# Micro Sensor Lab for CircuitPython

The Micro Sensor Lab is a little stack of sensors for use with a desktop computer, built up around an [Adafruit MCP2221](https://www.adafruit.com/product/4471) general purpose USB adapter board and the Adafruit Blinka library, which emulates [CircuitPython](https://circuitpython.org) on desktop and single board computer systems. The result is a compact stack of sensors that can be used for experimentation and hacking. This is useful in it's own right, since you can just write a little Python to get sensor data into your computer. It's also a nice input to interactive tools like [Processing](https://processing.org).

This code would also work fine with a standalone CircuitPython board. The beauty of using Blinka is the support it creates for moving from computer to microcontroller and back with little to no modifications to the code.

## Dependencies

First, to use this code as I intended, you're going to need Python 3 on your computer; I recommend Python 3.10 or newer. Why not be modern.

Next, you'll want to set up Blinka so you can talk to the MCP2221 over USB. Take a look at [this guide from Adafruit for setting up the MCP2221](https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-mcp2221).

Now it's time to install the library driver for the various sensors:

```
python install --updgrade adafruit-circuitpython-veml7700 adafruit-circuitpython-bme680 adafruit-circuitpython-lsm6ds adafruit-circuitpython-lis3mdl
```

Lastly, don't forget to set the environment variable to enable the MCP2221 support in Blinka:

```
export BLINKA_MCP2221="1"
```

Once this is done, give the code a try!