import React from "react";

const DeviceRow = ({ deviceName, keys }) => {
  return (
    <div>
      <div className="device-row">
        <span className="name">{deviceName}:</span>
        <span>
          {keys.map((key, index) => (
            <span key={index} style={{ marginRight: "1rem" }}>
              {key !== null
                ? `slot ${index + 1}: key ${key}`
                : `slot ${index + 1}: (empty)`}
            </span>
          ))}
        </span>
      </div>
    </div>
  );
};

export default DeviceRow;
