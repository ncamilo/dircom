#!/usr/bin/env python3
import serial.tools.list_ports
import argparse

VERSION = "1.0.1"

def list_serial_ports(usb_only=False):
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("No serial ports found.")
        return

    print("Available serial ports:")
    for p in ports:
        is_usb = p.vid is not None and p.pid is not None
        if usb_only and not is_usb:
            continue
        usb_flag = " [USB]" if is_usb else ""
        print(f"- {p.device} ({p.description}){usb_flag}")

def main():
    parser = argparse.ArgumentParser(
        description="List available serial (COM) ports on Windows, Linux & macOS."
    )
    parser.add_argument(
        "-u", "--usb-only",
        action="store_true",
        help="show only USB-connected ports"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {VERSION}"
    )
    args = parser.parse_args()
    list_serial_ports(usb_only=args.usb_only)

if __name__ == "__main__":
    main()
