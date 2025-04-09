class PrivateNetwork:
    '''
    keeps a set of network connection keys between devices.
    Each network connection has a unique network ID (int) and a tuple of device
    names.
    Each device can have up to 4 max network Ids.
    When a network is removed, the corresponding device networkId is set to None.
    New networks fills these None slots.
    '''
    def __init__(self):
        self.networks = {} # {"1": ["Alice", "Bob"]}
        self.devices = {} # {"Alice": [1,None,3,4]}
        self.network_count = 1 # next networkId if no recycled ids
        
    def add_key(self, devices: tuple) -> None:
        # Arg check
        if devices is None or len(devices) < 2:
            return
        # add network id to device
        for device in devices:
            if devices in self.devices:
                self.devices[device].append(self.network_count)
            else:
                self.devices[device] = [self.network_count]
        
        self.networks[str(self.network_count)] = list(devices)
        self.network_count += 1

    def get_devices(self) -> dict:
        return self.devices
    
    def get_networks(self) -> dict:
        return self.networks
    def get_network_count(self) -> int:
        return self.network_count