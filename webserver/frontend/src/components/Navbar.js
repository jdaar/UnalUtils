import React from "react"
import { Link } from "react-router-dom"

const Navbar = ({links}) => {
	return (
		<div className="navbar">
		{links.map(link => {
			return <Link to={link.route}><h3>{link.name}</h3></Link>
		})}
		</div>
	)
}

export default Navbar;