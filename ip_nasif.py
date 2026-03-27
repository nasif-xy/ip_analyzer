import ipaddress

def analyze_ip(ip):
    try:
        ip_obj = ipaddress.IPv4Address(ip)
        first_octet = int(ip.split('.')[0])

        # Identify Class
        if 1 <= first_octet <= 126:
            ip_class = "Class A"
            subnet = "255.0.0.0"
        elif 128 <= first_octet <= 191:
            ip_class = "Class B"
            subnet = "255.255.0.0"
        elif 192 <= first_octet <= 223:
            ip_class = "Class C"
            subnet = "255.255.255.0"
        elif 224 <= first_octet <= 239:
            ip_class = "Class D (Multicast)"
            subnet = "N/A"
        elif 240 <= first_octet <= 255:
            ip_class = "Class E (Experimental)"
            subnet = "N/A"
        else:
            ip_class = "Invalid"
            subnet = "N/A"

        # Private or Public
        if ip_obj.is_private:
            ip_type = "Private"
        else:
            ip_type = "Public"

        # Usable or not
        if ip_obj.is_loopback:
            usability = "Not usable (Loopback)"
        elif ip_obj.is_multicast:
            usability = "Not usable (Multicast)"
        elif ip_obj.is_reserved:
            usability = "Not usable (Reserved)"
        elif ip_obj.is_unspecified:
            usability = "Not usable (Unspecified)"
        else:
            usability = "Usable"

        # Output
        print(f"\nIP Address: {ip}")
        print(f"Class: {ip_class}")
        print(f"Default Subnet Mask: {subnet}")
        print(f"Type: {ip_type}")
        print(f"Usability: {usability}")

    except:
        print("Invalid IP Address!")

# Run program
ip = input("Enter IP Address: ")
analyze_ip(ip)