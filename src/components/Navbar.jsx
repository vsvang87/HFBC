import { useState } from "react";
import Contact from "../pages/Contact";
import Gallery from "../pages/Gallery";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div className="navbar-container">
      <div className="main-container">
        <nav className="navbar">
          <a href="#" className="logo">
            Hmong First Baptist Church
          </a>
          <ul className="nav-links">
            <li>
              <a href="#">About Us</a>{" "}
            </li>
            <li>
              <a href="#">Services</a>{" "}
            </li>
            <li>
              <a href="#">Contact</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
}

export default Navbar;
