import React from "react";
import { render } from "react-dom";
import Demo from "./demo";

import styles from "./cs/styles.scss";

function App() {
  return (
    <div className="App" style={{ padding: '20px' }}>
      <Demo />
    </div>
  );
}

const rootElement = document.getElementById("root");
render(<App />, rootElement);

