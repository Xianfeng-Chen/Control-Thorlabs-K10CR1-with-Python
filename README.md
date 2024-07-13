The codes are adopted from Thorlabs's official github account. The codes work for me in Spyder following the below steps:

1. **Install the Correct Version of Kinesis Software**
   - Visit the Thorlabs website to download the Kinesis software. Ensure you select the correct version based on your system: either 32-bit or 64-bit.

2. **First Time Connection with Kinesis Software**
   - Use the Kinesis software to connect to your device for the first time. This initial connection is necessary to avoid connection issues when using Python later.

3. **Modify Spyder Settings for clr Module**
   - It appears that Spyder has an issue with the `clr` module. To fix this, follow these steps:
     1. Open Spyder and go to the menu entry: **Tools > Preferences**.
     2. In the Preferences window, navigate to the **Python Interpreter** section.
     3. Click the button named **Set UMR excluded (not reloaded) modules**.
     4. In the dialog that appears, add `clr` to the list of excluded modules.

These steps should resolve the connection issues and ensure that the `clr` module functions correctly within Spyder.
