import React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./routes/Home";
import Register from "./routes/Register";
import Login from "./routes/Login";
import { FullSizeContainer } from "./components/Styled";

export const links = [
  {
    route: "/",
    name: "Inicio",
    component: Home,
  },
  {
    route: "/register",
    name: "Registrarse",
    component: Register,
  },
  {
    route: "/login",
    name: "Iniciar sesion",
    component: Login,
  },
];

const App = () => {
  return (
    <Router>
      <FullSizeContainer>
        <Switch>
          {links.map((link) => {
            return (
              <Route
                exact
                path={link.route}
                component={link.component}
                key={link.name}
              ></Route>
            );
          })}
        </Switch>
      </FullSizeContainer>
    </Router>
  );
};

render(<App />, document.getElementById("root"));
export default App;
