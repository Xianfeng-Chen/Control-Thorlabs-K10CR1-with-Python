# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:52:40 2024

@author: xfeng
"""

"""
K10CR1_pythonnet
==================

An example of using the K10CR1 integrated rotation stages with python via pythonnet
"""

import clr 
import os 
import time 
import sys

# Write in file paths of dlls needed. 
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.IntegratedStepperMotorsCLI.dll")

# Import functions from dlls. 
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.IntegratedStepperMotorsCLI import *
from System import Decimal 


def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:
        # Build device list.  
        DeviceManagerCLI.BuildDeviceList()

        # create new device.
        serial_no = "55416174"  # Replace this line with your device's serial number.
        device = CageRotator.CreateCageRotator(serial_no)
       
        # Connect to device. 
        device.Connect(serial_no)

        # Ensure that the device settings have been initialized.
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout.
            assert device.IsSettingsInitialized() is True

        # Start polling loop and enable device.
        device.StartPolling(250)  #250ms polling rate.
        time.sleep(0.25)
        device.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable.

        # Get Device Information and display description.
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Load any configuration settings needed by the controller/stage.
        device.LoadMotorConfiguration(serial_no, DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings)
        motor_config = device.LoadMotorConfiguration(serial_no)

        currentDeviceSettings = device.MotorDeviceSettings 
        print(currentDeviceSettings)
        
        velPars = device.GetVelocityParams();
        print(f'v={velPars.MaxVelocity}')
        
        newPos = device.Position
        print(f'position={newPos}')

        # Call device methods.
        print("Homing Device")
        device.Home(60000)  # 60 second timeout.
        print("Done")

        new_pos = Decimal(2.5)  # Must be a .NET decimal.
        print(f'Moving to {new_pos}')
        device.MoveTo(new_pos, 60000)  # 60 second timeout.
        print(f'position={device.Position}')
        #pos1 = device.GetCurrentPosition()
       # print("Done {pos1}")
        
        
        time.sleep(2)  # Wait for device to enable.
        new_pos2 = Decimal(5.0)  # Must be a .NET decimal.
        device.MoveTo(new_pos2, 60000)  # 60 second timeout.
        print("2nd move")
        print(f'position={device.Position}')
        
        time.sleep(2)  # Wait for device to enable.
        new_pos3 = Decimal(300.0)  # Must be a .NET decimal.
        device.MoveTo(new_pos3, 60000)  # 60 second timeout.
        print("3rd move")
        print(f'position={device.Position}')

        time.sleep(2)  # Wait for device to enable.
        new_pos4 = Decimal(1.0)  # Must be a .NET decimal.
        device.MoveTo(new_pos4, 60000)  # 60 second timeout.
        print("4th move")
        print(f'position={device.Position}')

        time.sleep(2)
        device.Home(60000)  # 60 second timeout.
        print(f'position={device.Position}')
        # Stop polling loop and disconnect device before program finishes. 
        device.StopPolling()
        device.Disconnect()

    except Exception as e:
        print(e)
        
    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UninitializeSimulations()


if __name__ == "__main__":
    main()