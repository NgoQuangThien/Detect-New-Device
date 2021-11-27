# DETECT NEW DEVICE 

## CentOS 7

###	Cài đặt các thành phần phụ thuộc
```
	$ cd dependencies
	$ sudo bash install.sh
```

###	Update kernel

####	Kiểm tra các version kernel hiện có
```
	$ sudo awk -F\' '$1=="menuentry " {print i++ " : " $2}' /etc/grub2.cfg
```

####	Thiết lập kernel mặc định
####	Sử dụng ID của kernel vừa cài - lấy từ câu lệnh kiểm tra phía trên để thay vào câu lệnh - ở đây giả sử với ID = 0)
```
	$ sudo grub2-set-default 0
	$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

####	Khởi động lại thiết bị
```
	$ sudo reboot
```

####	Kiểm tra lại version kernel đang sử dụng
```
	$ uname -snr
```

### Kích hoạt trình biên dịch

####	Kích hoạt llvm-toolset-7 và devtoolset-7
```
	$ scl enable llvm-toolset-7 bash
	$ scl enable devtoolset-7 bash
```

####	Kiểm tra version clang, gcc
```
	$ clang --version
	$ gcc --version
```

###	Chạy chương trình

####	Chương trình phía kernel (cần phải gán chương trình vào tất cả interface vật lý của thiết bị)
```
	$ cd kernel_program/main/
	$ make
	$ sudo ./xdp_pass_user --dev <interface_name> --auto-mode --force
```

####	Chương trình phía userspace
```
	$ cd userspace_program/
	$ sudo python3 main.py (chạy thử chương trình)
```

###	Chạy userspace program dưới dạng service
```
	$ cd userspace_program/install_service/
	$ sudo bash create_service.sh
```
