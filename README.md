## Installation
### Client only installtion
To control the pulser from a remote machine install only the client software with
```
git clone https://github.com/liviocali/2x2PulserSoft
cd 2x2PulserSoft
```
Now edit the IP of the pulser device in ```server_config.yaml```. Afterwards the software can be installed running
```
pip install . --client_only
```

### Installation on pulser device
#### Enable SPI
To run the pulser server on the built in Raspberry Pi SPI needs to be enabled.

First change boot config
```
sudo sed -i 's/#dtparam=spi=on/dtparam=spi=on/' /boot/config.txt
```
After this a reboot is needed
```
sudo reboot
```
Check if spi running
```
lsmod | grep spi_
```
#### Install software
```
git clone https://github.com/liviocali/2x2PulserSoft
cd 2x2PulserSoft
pip install .
```


#### Add server service
The server can be run using the ppulseserver command or adding a service to systemd.

The later is recommended. To set up the service do
```
sudo cp ppulseserver.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable ppulseserver
sudo systemctl restart ppulseserver
```
The server is now running on boot up of the pulser.

## Usage
To run the pulser first check that the device server is running
```
ppulse server-status
```
Now the pulse amplitude for each channel can be set running
```
set-channel -ch <channel_number> -s <serial_attenuator> -p <parallel_attenuator>
```
where ```<channel_number>``` is the output channel (1-16).
The pulser has a serial and parallel attenuator at the output stage of each channel. Those can be used to adjust the pulse amplitude. Set  ```<serial_attenuator>``` and ```<parallel_attenuator>``` from 0 to 255 where (255,0) is the highest amplitude (0,0) is the default amplitude and (0,255) is the lowest amplitude. Make sure ```s``` is already set to 0 before ```p``` is used to lower the amplitude more.