#Enable SPI
Change boot config
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

#Add server service
```
sudo cp ppulseserver.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable ppulseserver
sudo systemctl restart ppulseserver
```