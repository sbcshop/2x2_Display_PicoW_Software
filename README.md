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
<img src= "" />
  
### Interfacing Details




     

### Example Codes
   Try reference demo codes to test onboard components of HAT, make sure to save library file to run Serial Servo Motor related codes.
   - [Display Demo Code](https://github.com/sbcshop/Serial_Servo_Pico_HAT_Software/blob/main/examples/Demo_Display.py) : Visualize onboard display working with sample code
   - [BME280 Demo Code]() : BME280 sensor to read Temperature, humidity and pressure demo 
   - [RTC Demo](https://github.com/sbcshop/Serial_Servo_Pico_HAT_Software/blob/main/examples/Demo_Servo_mode.py) : Set and monitor real time clock activity 
   - [More..]()

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
