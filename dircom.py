import serial.tools.list_ports
import argparse

VERSION = "1.0.0"

def listar_portas_com(usb_only=False):
    portas = serial.tools.list_ports.comports()
    if not portas:
        print("Nenhuma porta COM encontrada.")
        return

    print("Portas COM disponíveis:")
    for porta in portas:
        is_usb = porta.vid is not None and porta.pid is not None
        if usb_only and not is_usb:
            continue
        usb_flag = " [USB]" if is_usb else ""
        print(f"- {porta.device} ({porta.description}){usb_flag}")

def main():
    parser = argparse.ArgumentParser(
        description="Listar portas seriais (COM) disponíveis no sistema."
    )
    parser.add_argument(
        "-u", "--usb-only", action="store_true", help="Listar apenas portas USB"
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {VERSION}"
    )

    args = parser.parse_args()
    listar_portas_com(usb_only=args.usb_only)

if __name__ == "__main__":
    main()
