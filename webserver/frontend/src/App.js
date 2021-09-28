import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './routes/Home';
import User from './routes/User';
import Register from './routes/Register'
import { FullSizeContainer } from './components/Styled';

const links = [
	{
		route: '/',
		name: 'Register',
		component: Register
	},
	{
		route: '/reg',
		name: 'Home',
		component: Home
	},
	{
		route: '/user',
		name: 'User info',
		component: User
	},
]

const App = () => {
	return (
		<Router>
			<FullSizeContainer>
				<Switch>
					{links.map(link => {
						return <Route exact path={link.route} component={link.component} key={link.name}></Route>
					})}
				</Switch>
			</FullSizeContainer>
		</Router>
	)
}

render(<App/>, document.getElementById('root'));
export default App;