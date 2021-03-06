# FastPM100
High speed acquisition and visualization of ThorLabs PM100 power meter
readings.

[![Travis Build Status](https://travis-ci.org/WasatchPhotonics/FastPM100.svg?branch=master)](https://travis-ci.org/WasatchPhotonics/FastPM100?branch=master)
[![Appveyor Build Status](https://ci.appveyor.com/api/projects/status/ruqnlbwuwl31lp6n/branch/master?svg=true)](https://ci.appveyor.com/project/NathanHarrington/FastPM100)
[![Coverage Status](https://coveralls.io/repos/WasatchPhotonics/FastPM100/badge.svg?branch=master&service=github)](https://coveralls.io/github/WasatchPhotonics/FastPM100?branch=master)

Specifications for the Thorlabs PM100 class laser power meters include
greater than 300 acquisitions per second. This project is designed to
show all readings the user for low pulse width laser power measurements.

FastPM100 provides two different modes of visualization:

    Basic strip chart
        Shows the last 3k readings and the current reading.

    Experimental visualization
        Heatmaps, multi line plots and other techniques to help
        visualize short duration laser power measurements.

# Experimental visualization mode

Experimental visualizations include the "AllController" mode, which will
display multiple sets of data from the [SlapChop](https://github.com/WasatchPhotonics/FastPM100/blob/master/fastpm100/devices.py):

![Simulated graph](/fastpm100/assets/images/simulated_graphs.gif "Simulated Graphs")


You can also use the [TripleVisualizer.bat](/scripts/TripleVisualizer.bat) file on windows to preposition the display windows:

![SlapChop Full screen screenshot](/fastpm100/assets/images/fullscreen.png "Full Screen")


# Basic strip chart mode

Consider the imagery below, which shows the difference between ThorLabs
Optical Power Meter software (v5.4) and FastPM100. This image was
captured using a Wasatch Photonics spectrometer under laser test with
two PM100 usb meters connected through a beamsplitter. The faster
sampling can prove invaluable when diagnosing complicated thermal,
electrical and reflective power interactions.

![FastPM100 comparison screenshot](/fastpm100/assets/images/application_screenshot.png "Comparison screenshot")


# Example use cases:

Temperature logging using the SlapChop:

First, setup the temperature recording script from BoardTester
in BoardTester/scripts/:

    python TemperatureLogger.py

To view all data on the local host:

    cd FastPM100
    python -u scripts/FastPM100.py --controller AllController

![SlapChop Long Term screenshot](/fastpm100/assets/images/long_term.png "Long Term")

To view one day of data, updating every ten seconds:

    python -u scripts/FastPM100.py 
        --controller AllController 
        --update 10000 
        --size 8640

Preload from a csv file, update every ten seconds:

    python -u scripts/FastPM100.py 
        --controller AllController 
        --file ../../BoardTester/scripts/combined_log.csv
        --update 10000
        --size 8640

Pre-position the window in the center of the screen, full width:

    python -u scripts/FastPM100.py 
        --controller AllController 
        --file ../../BoardTester/scripts/combined_log.csv
        --update 10000
        --size 8640
        --geometry 0,385,1920,333
        
Thorlabs PM100USB fast visualization:
configure the device as per the specifications below, then run:

    python -u scripts/FastPM100.py 

Run showing just the last 300 readings:

    python -u scripts/FastPM100.py --size 300




# Installation and testing setup

Running tests:

    First, install the python package in development mode:
        python setup.py develop

    All Tests, with coverage report showing missing lines:
        py.test tests/ --cov=fastpm100 --cov-report term-missing

    Certain tests are marked xfail to pass without access to the
    physical hardware. After the setup is performed below, run these
    with:

    py.test tests/test_thorlabs.py --hardware

Setup access to physical hardware:

    sudo -e /etc/udev/rules.d/99-thorlabs.rules

Add the following text:

    # Thorlabs PM100 USB
    SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="1313", ATTRS{idProduct}=="8072", MODE="0666"

Configure the power meter:

    For maximum reads per second, make sure to open the "Optical Power
    Meter" application from Thorlabs. Configure the device with the
    following settings:

    Range: turn off auto
    High gain
    No averaging
