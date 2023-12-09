A firmware is a low-level software embedded into electronic devices to operate the device, or bootstrap another program to do it.

Firmware exists in computers, peripherals (keyboards, mice, and printers), or even electronic home appliances.

In computers, the firmware provides a standard interface for complex software like an operating system to boot up and work with hardware components.

However, on simpler systems like a printer, the firmware is the operating system. The menu you use on your printer is the interface of its firmware.

Hardware manufacturers make firmware based on two specifications:

- **Basic Input/Output (BIOS)**
- **Unified Extensible Firmware Interface (UEFI)**

Firmwares - BIOS-based or UEFI-based - reside on a _non-volatile memory_, like a flash ROM attached to the motherboard.

MBR partitioning scheme is a part of the BIOS specifications and is used by BIOS-based firmware.

On MBR-partitioned disks, the first sector on the storage device contains essential data to boot up the system.

This sector is called MBR.

MBR contains the following information:

- The boot loader, which is a  **simple program**  (in machine code) to initiate the first stage of the booting process
- A  **partition table**, which contains information about your partitions.

![[Pasted image 20231208223317.png]]

#computing #computerarchitecture