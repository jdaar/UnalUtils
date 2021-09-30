import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import { HomeContainer } from "../components/Styled";
import Info from "./User/Info";
import { Route, Switch } from "react-router-dom";
import { links as generalLinks } from "../App";

const links = [
  {
    route: "/user/info",
    name: "Usuario",
    component: Info,
  },
];

const Home = () => {
  const [user, setUser] = useState({});

  useEffect(() => {
    fetch("/api/user", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${document.cookie
          .split(`; access=`)
          .pop()
          .split(";")
          .shift()
          .replace("access=", "")}`,
      },
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setUser(data);
      });
  }, []);

  return (
    <HomeContainer>
      <Navbar
        links={user.username ? links : generalLinks}
        username={user.username}
      ></Navbar>
      <Switch>
        {links.map((link) => {
          return (
            <Route
              exact
              path={link.route}
              key={link.name}
              component={link.component}
            ></Route>
          );
        })}
      </Switch>
    </HomeContainer>
  );
};

export default Home;
