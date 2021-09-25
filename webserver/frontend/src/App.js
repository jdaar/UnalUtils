import { render } from 'react-dom';
import React from 'react';

const App = () => {
	return (
		<p>Hello world</p>
	)
}

render(<App/>, document.getElementById('root'));
export default App;