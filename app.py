import ipaddress

print("Welcome to SubNetra Network Calculator!")

while True:
    giris = input("\nEnter a network address (e.g. 192.168.1.0/24 or 2001:db8::/64, enter q to quit): ").strip()
    if giris.lower() == "q":
        break
    if not giris:
        giris = "192.168.1.0/24"
        print(f"Empty input, using default: {giris}")

    try:
        if "/" in giris:
            ag = ipaddress.ip_network(giris, strict=False)
        else:
            tek_ip = ipaddress.ip_address(giris)
            ag = ipaddress.ip_network(f"{tek_ip}/{32 if isinstance(tek_ip, ipaddress.IPv4Address) else 128}", strict=False)
    except ValueError as e:
        print(f"Invalid address: {e}")
        continue

    if isinstance(ag, ipaddress.IPv6Network):
        print(f"IP version:          IPv6")
        print(f"Network address:     {ag.network_address}")
        print(f"CIDR notation:       {ag.with_prefixlen}")
        print(f"Prefix length:       {ag.prefixlen}")
        print(f"Total IP count:      {ag.num_addresses}")
        print(f"Is private:          {ag.is_private}")
        print(f"Is loopback:         {ag.is_loopback}")
        print(f"Is link-local:       {ag.is_link_local}")
        print(f"Integer ID:          {int(ag.network_address)}")
        print(f"HEX ID:              {hex(int(ag.network_address))}")

    else:
        if ag.prefixlen < 31:
            host_sayisi = ag.num_addresses - 2
            ilk = ag.network_address + 1
            son = ag.broadcast_address - 1
        elif ag.prefixlen == 31:  
            host_sayisi = 2
            ilk = ag.network_address
            son = ag.broadcast_address
        else:  # /32
            host_sayisi = 1
            ilk = ag.network_address
            son = ag.network_address

        ilk_oktet = int(ag.network_address.packed[0])
        if 0 <= ilk_oktet <= 127:
            ip_sinifi = "A"
        elif 128 <= ilk_oktet <= 191:
            ip_sinifi = "B"
        elif 192 <= ilk_oktet <= 223:
            ip_sinifi = "C"
        elif 224 <= ilk_oktet <= 239:
            ip_sinifi = "D (Multicast)"
        else:
            ip_sinifi = "E (Experimental)"

        print(f"IP version:          IPv4")
        print(f"Network address:     {ag.network_address}")
        print(f"Broadcast address:   {ag.broadcast_address}")
        print(f"Subnet mask:         {ag.netmask}")
        print(f"Wildcard mask:       {ag.hostmask}")
        print(f"Binary subnet mask:  {bin(int(ag.netmask))}")
        print(f"IP class:            {ip_sinifi}")
        print(f"Prefix length:       {ag.prefixlen}")
        print(f"IP type:             {'Private' if ag.is_private else 'Public'}")
        print(f"CIDR notation:       {ag.with_prefixlen}")
        print(f"Binary ID:           {bin(int(ag.network_address))}")
        print(f"Integer ID:          {int(ag.network_address)}")
        print(f"HEX ID:              {hex(int(ag.network_address))}")
        print(f"Usable hosts:        {host_sayisi}")
        print(f"Total host count:    {ag.num_addresses}")
        print(f"First host:          {ilk}")
        print(f"Last host:           {son}")
        print(f"Is private network:  {ag.is_private}")

        if host_sayisi <= 33 and host_sayisi > 0:
            print("All hosts:", ", ".join(str(h) for h in ag.hosts()))
        else:
            print("(Host count is too large or not suitable for listing.)")