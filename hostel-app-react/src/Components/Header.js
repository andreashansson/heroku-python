import React from 'react';
import logo from '../images/logo.png';
import '../css/Header.css';
const Header = () => {
	return (
		<header className="Header">
			<div className="Logo"><img src={logo} alt="logo" /></div>
			<ul className="Menu">
				<li>Home</li>
				<li>Packages</li>
				<li>Rooms</li>
				<li>Booking</li>
				<li>Contact</li>
			</ul>
		</header>
	)
}

export default Header;