import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './routes/Home';
import User from './routes/User';

const links = [
	{
		route: '/',
		name: 'Home',
		component: Home
	},
	{
		route: '/user',
		name: 'User info',
		component: User
	}
]

const App = () => {
	return (
		<Router>
			<Navbar links={links}/>
			<Switch>
				{links.map(link => {
					return <Route exact path={link.route} component={link.component}></Route>
				})}
			</Switch>
		</Router>
	)
}

render(<App/>, document.getElementById('root'));
export default App;