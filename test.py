

def testAddSingleKey():
    test = PrivateNetwork()
    test.add_key(("Alice", "Bob"))
    devices = test.get_devices()
    network = test.get_networks()
    count = test.get_network_count()
    test.print_networks()

    # test network count
    assert count == 2, "Network count should be at 2 after adding one connection"
    # test devices
    assert "Alice" in devices, "Alice should be in devices list"
    assert "Bob" in devices, "Bob should be in devices list"
    # test network
    assert "1" in network, "Network should contain one key, val pair of '1': ('Alice', 'Bob')"
    assert network["1"] == ["Alice", "Bob"], "Network should contain one key, val pair of '1': ('Alice', 'Bob')"

def testAddTwoKeys():
    test = PrivateNetwork()
    test.add_key(("Alice", "Bob"))
    test.add_key(("Carlos", "Alice"))
    devices = test.get_devices()
    network = test.get_networks()
    count = test.get_network_count()

    # test count
    assert count == 3, "Count should be at 3 after adding 2 networks"
    # test devices
    assert "Alice" in devices and "Bob" in devices and "Carlos" in devices, "Alice, Bob, and Carlos should be in devices"
    
    # test networks
    assert "1" in network and "2" in network, "Network should have 1 and 2"
    assert ("Alice", "Bob") in network.values() or ("Bob", "Alice") in network.values(), "Alice and Bob should be a pair in network"
    assert ("Alice", "Carlos") in network.values() or ("Carlos", "Alice") in network.values(), "Alice and Carlos should be a pair in network"
    
def testAddMultipleKeys():
    test = PrivateNetwork()
    test.add_key(("Alice", "Bob"))
    test.add_key(("Alice", "Carlos"))
    test.add_key(("Alice", "David"))
    test.add_key(("Alice", "Bob", "Carlos", "David"))
    test.add_key(("Bob", "Carlos", "David"))
    test.add_key(("Bob", "Alice"))

    devices = test.get_devices()
    network = test.get_networks()
    count = test.get_network_count()
    
    # test devices list
    assert "Alice" in devices, "Alice should be in the devices list."
    assert "Bob" in devices, "Bob should be in the devices list."
    assert "Carlos" in devices, "Carlos should be in the devices list."
    assert "David" in devices, "David should be in the devices list."

    # test network list
    for i in range(0, 4):
        assert str(i+1) in network
    assert "6" not in network

    assert ("Alice", "Bob") in network.values() or ("Bob", "Alice") in network.values(), "Network must include connection between Alice and Bob."
    assert ("Carlos", "Alice") in network.values() or ("Alice", "Carlos") in network.values(), "Network must include connection between Alice and Carlos."
    assert ("David", "Alice") in network.values() or ("Alice", "David") in network.values(), "Network must include connection between Alice and David."
    assert ("Alice", "Bob", "Carlos", "David") in network.values(), "Network must include connection between all 4."
    assert ("Bob", "Carlos", "David") in network.values(), "Network must include connection excluding Alice."
    assert 6 not in devices["Alice"] and 6 not in devices["Bob"], "Alice -> Bob must only have one unique pair."
    # Check that count is as expected, e.g., 1
    assert count == 6, "Network count should be 6 after adding up to last connection and failing to add last."
