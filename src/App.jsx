import { useState } from "react";
import Navbar from "./components/Navbar";
import Intro from "./components/Intro";
import Section1 from "./components/Section1";
import "./css/style.css";
//
function App() {
  return (
    <div className="App">
      <Navbar />
      <Intro />
      <Section1 />
    </div>
  );
}

export default App;
