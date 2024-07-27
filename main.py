import socket


def scan_port(ip, port, timeout=0.1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False


def scan_ports(ip, start_port, end_port, timeout=0.1):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port, timeout):
            open_ports.append(port)
    return open_ports


# Example usage
if __name__ == "__main__":
    ip_address = input("Enter the IP address to scan: ")

    # Take the starting port input
    while True:
        try:
            start_port = int(input("Enter the starting port (1-65535): "))
            if 1 <= start_port <= 65535:
                break
            else:
                print("Please enter a valid port number between 1 and 65535.")
        except ValueError:
            print("Please enter a valid integer.")

    # Take the ending port input
    while True:
        try:
            end_port = int(input("Enter the ending port (1-65535): "))
            if 1 <= end_port <= 65535 and end_port >= start_port:
                break
            else:
                print(
                    "Please enter a valid port number between 1 and 65535, and it should be greater than or equal to the starting port.")
        except ValueError:
            print("Please enter a valid integer.")

    print(f"Scanning {ip_address} from port {start_port} to {end_port}...")
    open_ports = scan_ports(ip_address, start_port, end_port)

    if open_ports:
        print(f"Open ports on {ip_address}: {open_ports}")
    else:
        print(f"No open ports found on {ip_address} in the range {start_port}-{end_port}.")
