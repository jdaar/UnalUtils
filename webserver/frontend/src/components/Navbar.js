import React from "react"
import { Link } from "react-router-dom"
import { Button } from "./Styled"

const Navbar = ({links}) => {
	return (
		<div className="navbar">
		{links.map(link => {
			return <Link to={link.route}><Button>{link.name}</Button></Link>
		})}
		</div>
	)
}

export default Navbar;