import React, { useState, useEffect } from "react";
import Row from "./components/row";
import DeviceRow from "./components/DeviceRow";
import "./App.css";

function App() {
  const [networkData, setNetworkData] = useState({
    networks: {},
    devices: {},
    next_network: 1,
  });
  const [devicesInput, setDevicesInput] = useState("");
  const [nextNetwork, setNextNetwork] = useState(1);

  const fetchMockData = () => {
    fetch("http://127.0.0.1:8000")
      .then((res) => res.json())
      .then((data) => setNetworkData(data))
      .catch((err) => console.error("Error fetching data:", err));
  };

  // Load on mount
  useEffect(() => {
    fetchMockData();
  }, []);

  // post request for new connection
  const handleSubmit = (e) => {
    e.preventDefault();
    const devices = devicesInput.split(",").map((s) => s.trim());
    // send to fastapi backend
    fetch("http://127.0.0.1:8000/add_key", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ devices }),
    })
      .then((res) => res.json())
      .then((data) => {
        setNetworkData(data);
        setDevicesInput("");
      })
      .catch((err) => console.error("Error posting data:", err));
  };

  return (
    <div className="container">
      <section className="data-container">
        <div className="networks">
          <h1>Network Keys</h1>

          <h2>Current Networks and Keys</h2>
          <div>
            {Object.entries(networkData.networks).map(
              ([networkId, devices]) => (
                <Row key={networkId} networkId={networkId} devices={devices} />
              )
            )}
          </div>
        </div>
        <div className="devices">
          <h1>Devices</h1>

          <h2>Current Devices</h2>
          <div>
            {Object.entries(networkData.devices).map(([deviceName, keys]) => (
              <DeviceRow key={deviceName} deviceName={deviceName} keys={keys} />
            ))}
          </div>
        </div>
      </section>

      <div className="add-key">
        <h2>Add a New Key</h2>
        <form onSubmit={handleSubmit}>
          <label>
            Enter device names (comma separated):{" "}
            <input
              type="text"
              value={devicesInput}
              onChange={(e) => setDevicesInput(e.target.value)}
              placeholder="e.g., Alice, Bob"
            />
          </label>
          <button type="submit" style={{ marginLeft: "1rem" }}>
            Add Key
          </button>
        </form>
      </div>
    </div>
  );
}

export default App;
