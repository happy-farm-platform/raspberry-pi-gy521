# raspberry-pi-gy521
Raspberry PI GY-521 MPU6050 gyroscope triaxial 

**Running**
```commandline
python gyro.py
```
This command will collect 10,000 orientation samples in the format row,pitch,yaw (x,y,z) in the console output. 
The axes are printed on the board. 
For more information about roll, pitch, and yaw check the [wikipedia](https://en.wikipedia.org/wiki/Aircraft_principal_axes).

**Pre-requisites**
* [Enable I2C and install utilities on raspberry-pi](https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/)
* [Connect your MPU6050 GY-521 to the GPIO](https://www.researchgate.net/figure/Connection-diagram-for-the-MPU6050-accelerometer-to-Raspberry-Pi-Zero-Figure-made_fig4_351761565)

**Calibration**

All boards are different each other from the fabric, and they need to be calibrated.
Follow the calibration procedure
* Put your sensor in a stable place (e.g. your table)
* Run ```python MPU6050_cal.py```
* Wait ~1 min

The values will be printed in the output, use it to replace the values in the `gyro.py`.

Sample output:
```commandline
acceleration calibration
x_avg_read: 187.28 x_avg_offset: -430.6145
y_avg_read: -427.4 y_avg_offset: 958.84825
z_avg_read: 258.92 z_avg_offset: -258.02375
gyro calibration
x_avg_read: -22.14 x_avg_offset: 33.129625
y_avg_read: 0.92 y_avg_offset: 41.6715
z_avg_read: 1.23 z_avg_offset: 5.2561875

```
Use only the natural numbers as follows:
```python
x_accel_offset = -430
y_accel_offset = 958
z_accel_offset = -258
x_gyro_offset = 33
y_gyro_offset = 41
z_gyro_offset = 5
```
