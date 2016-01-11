""" Simulated device components for demonstration program. Simple blocking calls
with simulated delays for simulated spectrometer readings. Long-polling
multiprocessing wrappers.
"""

import time
import Queue
import numpy
import logging
import multiprocessing

from ThorlabsPM100 import ThorlabsPM100, USBTMC

from . import applog

log = logging.getLogger(__name__)


# USBTMC instruments

# Agilent MSO7104
#SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="0957", ATTRS{idProduct}=="1755", GROUP="usbtmc", MODE="0660"

class ThorlabsMeter(object):
    """ Create a simulated laser power output meter.
    """
    def __init__(self, noise_factor=1.0):
        super(ThorlabsMeter, self).__init__()
        log.debug("%s setup", self.__class__.__name__)

        self.inst = USBTMC(device="/dev/usbtmc0")
        self.power_meter = ThorlabsPM100(inst=self.inst)
        self.power_meter.sense.correction.wavelength = 785.0

    def read(self):
        return self.power_meter.read

class SimulatedPM100(object):
    """ Create a simulated laser power output meter.
    """
    def __init__(self, noise_factor=1.0):
        super(SimulatedPM100, self).__init__()
        log.debug("%s setup", self.__class__.__name__)

        self.noise_factor = noise_factor
        self.counter = 0.1234567

    def increment_counter(self):
        """ Add a value to return value.
        """
        self.counter += 0.000001
        value = 123.0 + self.counter
        return value

    def read(self):
        """ Return the test-specific pattern.
        """
        return self.increment_counter()

    def apply_noise(self):
        """ Return a single value with noise applied.
        """

        value = 123.0 + numpy.random.uniform(0, self.noise_factor, 1)
        value = value[0]
        #log.debug("Return: %s" % value)
        return value

class SubProcessSimulatedPM100(object):
    """ Wrap simulate pm100 in a non-blocking interface run in a separate
    process.
    """
    device_class = SimulatedPM100

    def __init__(self, log_queue=None):
        self.response_queue = multiprocessing.Queue()
        self.command_queue = multiprocessing.Queue()

        args = (log_queue, self.command_queue, self.response_queue)
        self.poller = multiprocessing.Process(target=self.continuous_poll,
                                              args=args)
        self.poller.start()

    def close(self):
        """ Add the poison pill to the command queue.
        """
        self.command_queue.put(None)
        self.poller.join(0.1)     # Required on Windows
        self.poller.terminate() # Required on windows
        log.debug("Post poller terminate")

    def continuous_poll(self, log_queue, command_queue, response_queue):

        applog.process_log_configure(log_queue)

        self.device = self.device_class()

        total_reads = 0

        # Read forever until the None poison pill is received
        while True:

            data = self.device.read()
            total_reads += 1
            response_queue.put_nowait((total_reads, data))
            time.sleep(0.0001)
            #log.debug("Collected data in continuous poll %s" % total_reads)

            try:
                record = command_queue.get_nowait()
                if record is None:
                    log.debug("Exit command queue")
                    break

            except Queue.Empty:
                #log.debug("Queue empty")
                #time.sleep(0.1001)
                pass

            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                import sys, traceback
                print >> sys.stderr, 'Whoops! Problem:'
                traceback.print_exc(file=sys.stderr)

    def read(self):
        """ Don't use if queue.empty() for flow control on python 2.7 on
        windows, as it will hang. Use the catch of the queue empty exception as
        shown below instead.
        """
        result = None
        try:
            result = self.response_queue.get_nowait()
        except Queue.Empty:
            pass

        return result

class SubProcessThorlabsMeter(SubProcessSimulatedPM100):
    """ Wrap an actual thorlabs pm100 in a non-blocking interface run in a
    separate process.
    """
    device_class = ThorlabsMeter
