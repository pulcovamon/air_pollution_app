import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import { IoClose, IoMenu } from "react-icons/io5";

export default function Navbar() {
    return (
        <header className="header">
          <nav className="nav container">
            <NavLink to="/" className="nav__logo">
              Air Quality Monitoring App
            </NavLink>
     
            <div
              className={"nav__menu"}
              id="nav-menu"
            >
              <ul className="nav__list">
                <li className="nav__item">
                  <NavLink to="/" className="nav__link">
                    Air Quality Index
                  </NavLink>
                </li>
                <li className="nav__item">
                  <NavLink to="/parameters" className="nav__link">
                    Air Qualty Parameters
                  </NavLink>
                </li>
                <li className="nav__item">
                  <NavLink
                    to="/statistics"
                    className="nav__link"
                  >
                    Statistics
                  </NavLink>
                </li>
                <li className="nav__item">
                  <NavLink
                    to="/city-comparison"
                    className="nav__link"
                  >
                    City Comparison
                  </NavLink>
                </li>
              </ul>
              <div className="nav__close" id="nav-close">
                <IoClose />
              </div>
            </div>
     
            <div className="nav__toggle" id="nav-toggle">
              <IoMenu />
            </div>
          </nav>
        </header>
      );
   }
   