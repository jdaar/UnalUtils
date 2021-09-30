import React from "react";
import { useLocation, useHistory } from "react-router-dom";
import {
  LinkList,
  LinkListElement,
  LinkListElementLink,
  NavbarContainer,
  NavbarContainerWrapper,
  NavbarTitle,
  NavbarTitleAnnotation,
} from "./Styled";

const Navbar = ({ links, username }) => {
  const location = useLocation();
  const history = useHistory();

  const removeCookie = () => {
    const setCookie = (name, value, minutes) => {
      const date = new Date();
      date.setTime(date.getTime + minutes * 60 * 1000);
      document.cookie = `${name}=${value}; path=/; expires=${date.toUTCString()};`;
    };
    setCookie("access", "", 0);
    history.go(0);
  };
  return (
    <NavbarContainer>
      <NavbarContainerWrapper>
        {username ? (
          <NavbarTitle>
            Bienvenido,{" "}
            <NavbarTitleAnnotation>{username}</NavbarTitleAnnotation>
          </NavbarTitle>
        ) : (
          <NavbarTitle>
            Unal utils
            <NavbarTitleAnnotation>{username}</NavbarTitleAnnotation>
          </NavbarTitle>
        )}
        <LinkList>
          {links.map((link) => {
            return (
              <LinkListElement>
                <LinkListElementLink
                  to={link.route}
                  color={link.route == location.pathname ? "#FFF" : "#D8247C"}
                >
                  {link.name}
                </LinkListElementLink>
              </LinkListElement>
            );
          })}
          {username ? (
            <LinkListElement onClick={removeCookie}>
              <LinkListElementLink to={location.pathname}>
                Cerrar sesion
              </LinkListElementLink>
            </LinkListElement>
          ) : undefined}
        </LinkList>
      </NavbarContainerWrapper>
    </NavbarContainer>
  );
};

export default Navbar;
