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
        
        # if connection already exists, dont add
        if self._connection_exists(devices):
            return
        
        # add network id to device
        for device in devices:
            if device in self.devices:
                if len(self.devices[device]) < 4:
                    self.devices[device].append(self.network_count)
                else:
                    continue
            else:
                self.devices[device] = [self.network_count]
        
        self.networks[str(self.network_count)] = devices
        self.network_count += 1

    def get_device_keys(self, device: str):
        """
        Returns the list of network keys for a given device.
        
        param 
            - device: Device name
        return: 
            - List of network ids (int) or empty list if unknown
        """
        return self.devices.get(device, [])

    def get_networks(self):
        """
        Returns the dictionary of networks.

        return:
            - dict of networks
        """
        return self.networks

    def get_devices(self):
        """
        Returns the dictionary of devices.

        return:
            - dict of devices
        """
        return self.devices

    def get_network_count(self):
        """
        Returns the next available network ID.

        return:
            - int: network count
        """
        return self.network_count
    
    def print_networks(self) -> None:
        """
        Prints out all networks with each device. Each device prints its slot
        that contains the network ID.
        """
        for network_id, connection in self.networks.items():
            print(f"Network {network_id},key {network_id}:")
            for device in connection:
                device_keys = self.get_device_keys(device)
                # slots should print at ind 1 start (slot 1 is index 0)
                slot = device_keys.index(int(network_id)) + 1
                print(f"\t{device} - put key {network_id} in slot {slot}")

    
    def _connection_exists(self, new_connection: tuple) -> bool:
        """
        Checks if a connection for a given pair already exists.
        
        param:
            - new_connection: Tuple of device names.
        return: 
            - True if the connection already exists, otherwise False.
        """
        for connection in self.networks.values():
            if self._connections_equal(connection, new_connection):
                return True
        return False

    @staticmethod
    def _connections_equal(existing: tuple, new: tuple) -> bool:
        """
        Compares two device tuples regardless of order.
        
        param 
            - existing: An existing network connection.
            - new: A new network connection.
        return: 
            - True if they contain the same devices, False otherwise.
        """
        return sorted(existing) == sorted(new)