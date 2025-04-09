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
        self.free_networks = [] # list of recylced network ids
        
    def add_key(self, devices: tuple) -> None:
        # Arg check
        if devices is None or len(devices) < 2:
            return
        
        # Do base case checks:
        # if any device already has 4 keys and no None, do not add
        if self._any_device_at_max(devices):
            return

        # if connection already exists, dont add
        if self._connection_exists(devices):
            return
        
        # extract either next network id or a recycled one
        if self.free_networks:
            network_id = self.free_networks.pop() # pop last element for O(1) time
        else:
            network_id = self.network_count
            self.network_count += 1
        # update each devices key list
        for device in devices:
            if device in self.devices:
                if len(self.devices[device]) < 4:
                    self.devices[device].append(network_id)
                else:
                    # find the first available None slot and fill it
                    for i, key in enumerate(self.devices[device]):
                        if key is None:
                            self.devices[device][i] = network_id
                            break
            else:
                # init new device with its list as current network_id
                self.devices[device] = [network_id]

        # save new network connection
        self.networks[str(network_id)] = devices

    def remove_key(self, network: int) -> None:
        """
        Removes network connection with the given network ID.
        For each device in connection, sets the matching key entry to None.
        The removed network ID is added to the free_networks list for reuse.
        
        param:
            - network: network ID to remove
        """
        network_key = str(network)
        if network_key not in self.networks:
            return
        
        devices_in_network = self.networks.pop(network_key)
        if not devices_in_network:
            return

        for device in devices_in_network:
            if device in self.devices:
                try:
                    index = self.devices[device].index(network)
                    self.devices[device][index] = None
                except ValueError:
                    # network was not recorded for this device
                    pass
        
        self.free_networks.append(network)

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
    
    def _any_device_at_max(self, devices: tuple) -> bool:
        """
        Returns True if any device in the devices tuple already has 4 keys 
        with no available (None) slot.
        
        param 
            - devices: Tuple of device names.
        return: 
            - True if at least one device cannot accept a new network key.
        """
        for device in devices:
            if device in self.devices:
                keys = self.devices[device]
                # if theres room, then not maxed
                if len(keys) < 4:
                    continue
                # if no slot is None, its full
                if None not in keys:
                    return True
        return False

    def is_max_keys(self, device: str) -> bool:
        """
        Returns true if the device has 4 keys with no None slot.
        
        param:
            - device: Device name.
        return: 
            - True if device is at maximum capacity.
        """
        if device not in self.devices:
            return False
        keys = self.devices[device]
        return len(keys) >= 4 and None not in keys