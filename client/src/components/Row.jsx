import React from "react";

const Row = ({ networkId, devices }) => {
  return (
    <div className="row">
      <div className="row-data">
        Network {networkId}, key {networkId}:
        <span>
          {devices.map((device, index) => (
            <span key={index}>{device}</span>
          ))}
        </span>
      </div>
    </div>
  );
};

export default Row;
