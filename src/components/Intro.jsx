import { useState } from "react";
import jesus from "../images/bible.jpg";
import groupImg from "../images/group.jpg";

function Intro() {
  return (
    <div
      className="intro-container"
      style={{
        backgroundImage: `url(${groupImg})`,
        backgroundRepeat: "no-repeat",
        backgroundPosition: "center",
        backgroundSize: "cover",
      }}
    >
      <div className="main-container">
        <div className="intro-content">
          <p className="lg-text">
            "With man this is impossible, but with God all things are possible."
            -Matthew 19:26
          </p>
        </div>
      </div>
    </div>
  );
}

export default Intro;
