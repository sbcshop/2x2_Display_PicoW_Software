# 2x2_Display_PicoW_Software

<img src= "https://cdn.shopify.com/s/files/1/1217/2104/files/Main_Pico_Banner.png?v=1720594366" />

The Quad Display Board features four displays in a single board, offering unparalleled flexibility and functionality for your creative endeavors. With options for both a 1.28" Round Display and a 1.54" Square Display, you have the freedom to choose the perfect size for your project needs. 

This github provides getting started guide for both Round and Square 2x2 Display with Pico W.

### Features:
- Powered by Raspberry Pi  Pico W microcontroller which is having Dual-core Arm Cortex-M0+ processor, running up to 133 MHz
- Four Square/Round Display in 2x2 arrangement for creative visual interactions
- DS3231 RTC for real-time capture and control activity With Backup Battery Holder
- BME280 Sensor for temperature, humidity and pressure monitoring
- Power and Charging LED for status indication
- Battery hookup and charging facilities for portability
- Onboard microSD card compatibility is useful for data logging purposes
- Multipurpose GPIOs breakout for additional peripheral interfacing
- Four Programmable Buttons to add additional controls to project 
- Buzzer which helps to add audio alert for your project

### Specifications:
- **Microcontroller:** [Raspberry Pi Pico W](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/Documents/pico-w-datasheet.pdf)
- **Connectivity:** WiFi & BLE
- **Memory:** 264kB on-chip SRAM, 2MB on-board QSPI flash
- **Supply Voltage:** 5V
- **Operating pin voltage:** 3.3V
- **Display:** 
  - Display Size: 1.54” (Square), 1.28” (Round) 
  - Display Type: IPS TFT 
  - Display Resolution:  240 x 240 pixels
  - Display colors: 65K RGB
  - Display interface: SPI
  - Display Driver: **ST7789V** (Square), **GC9A01A** (Round)
- **Sensor**: [BME280](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/Documents/BME280-Datasheet.pdf) for Temperature, Pressure & Relative Humidity
- **RTC Chip**: [DS3231SN](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/Documents/ds3231.pdf)
- **RTC Battery Holder**: Supports CR1220 3V Battery 
- **Operating Temperature Range**: -20°C ~ +70°C

## Getting Started with 2x2 Display with Pico W
### Pinout
<img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/2x2_display_picow_pinout.png" />
  
### Interfacing Details
- Following GPIO pins of Raspberry Pi Pico W is used for onboard components,
  
  <img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/2x2_display_picow_hardware_interfacing.png" width="754" height="413" />

  **Note:**
  * Backlight pin common for all display
  
- _**GPIOs Breakout**_
  | Pico | Function |
  |---|---|
  | 3V3 | Supply 3.3V  |
  | GP0 | Multipurpose GPIO |
  | GP1 | Multipurpose GPIO |
  | GND | Supply Ground |
  
### 1. How to Install Boot Firmware in Pico W 

- Every board will be pre-installed with suitable MicroPython firmware with the inbuilt display driver module, so you can skip this step and jump to [**Step 2**](https://github.com/sbcshop/2x2_Display_PicoW_Software/tree/main#2-running-first-program) for trying Demo Codes.
- In any case, you want to add again **MicroPython firmware**. First, you need to *Press and Hold* the boot button on pico W, and then, without releasing the button, connect it to PC/laptop using micro USB cable. Check below image for reference,
  
  <img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/pico_bootmode.gif" width="340" height="228">

- Now your device is in boot mode, and you will see a new mass storage device named "RPI-RP2" as shown in the below figure.

  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>

- Download the relevant MicroPython firmware file provided in this repo above,
  - For 1.54" Square Variant - ["**_firmware_2x2display_picow_square.uf2_**"](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/firmware_2x2display_picow_square.uf2)
  - For 1.28" Round Variant - ["**_firmware_2x2display_picow_round.uf2_**"](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/firmware_2x2display_picow_round.uf2)
    
  Drag and drop Firmware file onto the RPI-RP2 volume.

  <img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/firmware_install.png" width="740" height="463">
  
### 2. Running First Program
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Download this github which contains various examples and open anyone of example in Thonny.

     <img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/github_download.png" width="767" height="386" />
   - Now we have **Thonny IDE application** and github example codes, Connect hardware to laptop/PC. Open any example code in Thonny IDE. Then select micropython device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.

     <img src="https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/select_device.png" width="448" height="196">
  
   - Make sure to save [_**lib**_]() folder which contains dependent library file to device to avoid any execution error.

      <img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/lib_save.png" />

   - Once everything all set, with any demo code open click on green play button to test program.

     <img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/run_script.png" />

   - For standalone execution save script into Pico as main.py,

     <img src= "https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/images/main_save.png" />

     Try out below provided reference example demo codes and modify to build your own application codes.
     

### Example Codes
   Try reference demo codes to test onboard components, also make sure to save lib folder into Pico W of board which contains library files.
   - For 1.54" Square Display Variant
     - [Display Demo Code](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/examples/2x2_Display_PicoW_Square1_54/Demo_4Display.py) : Visualize onboard display working with sample code
     - [BME280 Sensor](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/examples/2x2_Display_PicoW_Square1_54/Demo_BME280.py) : BME280 sensor to read Temperature, humidity and pressure demo
     - [More...](https://github.com/sbcshop/2x2_Display_PicoW_Software/tree/main/examples/2x2_Display_PicoW_Square1_54)
       
   - For 1.28" Round Display Variant
     - [Display Image](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/examples/2x2_Display_PicoW_Round1_28/Demo_DisplayImage.py) : Visualize onboard display working with sample code
     - [RTC Code](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/examples/2x2_Display_PicoW_Round1_28/Demo_RTC_BME280.py) : Set and Read real time clock activity along with temperature, pressure and humidity measure
     - [More...](https://github.com/sbcshop/2x2_Display_PicoW_Software/tree/main/examples/2x2_Display_PicoW_Round1_28)

   Using this sample code as a guide, you can modify, build, and share codes!!
   
## Resources
  * [Schematic](https://github.com/sbcshop/2x2_Display_PicoW_Hardware/blob/main/Design%20Data/2x2_Display_PicoW_SCH.pdf)
  * [Hardware Files](https://github.com/sbcshop/2x2_Display_PicoW_Hardware)
  * [Step File](https://github.com/sbcshop/2x2_Display_PicoW_Hardware/blob/main/Mechanical%20Data/2X2_Display_PicoW.step)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [Raspberry Pico Datasheet](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/Documents/pico-w-datasheet.pdf)
  * [DS3231 RTC Datasheet](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/Documents/ds3231.pdf)
  * [BME280 Sensor Datasheet](https://github.com/sbcshop/2x2_Display_PicoW_Software/blob/main/Documents/BME280-Datasheet.pdf)


## Related Products  
  * [2x2 Display with ESP32 S3 (Round)](https://shop.sb-components.co.uk/products/2x2-quad-display-board?variant=41538301493331)

    ![2x2 Display with ESP32 S3 (Round)](https://shop.sb-components.co.uk/cdn/shop/files/mainroundesp32.png?v=1720527042&width=300)
    
  * [2x2 Display with ESP32 S3 (Square)](https://shop.sb-components.co.uk/products/2x2-quad-display-board?variant=41538301526099)

    ![2x2 Display with ESP32 S3 (Square)](https://shop.sb-components.co.uk/cdn/shop/files/mainsquareesp32.png?v=1720527077&width=300)
    
  * [Touchsy - 3.2" Touch LCD Display Based on Pico W](https://shop.sb-components.co.uk/products/touchsy-3-2-touch-lcd-display-based-on-pico-w?variant=40828148744275)

    ![Touchsy - 3.2" Touch LCD Display Based on Pico W](https://shop.sb-components.co.uk/cdn/shop/files/touchsypicowresitive.jpg?v=1686903806&width=300)
  
  * [Rotary Encoder - LED Array & Touch LCD Powered by Pico W](https://shop.sb-components.co.uk/products/rotary-encoder-led-array-touch-lcd-for-esp32-pico-hat?variant=41002601676883)

    ![Rotary Encoder - LED Array & Touch LCD Powered by Pico W](https://shop.sb-components.co.uk/cdn/shop/files/RotaryEncoder-LEDArray_TouchLCDforESP32PicoHAT_7.png?v=1710413189&width=300)


## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
