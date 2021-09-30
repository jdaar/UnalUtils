import { Link } from "react-router-dom";
import styled, { css, keyframes } from "styled-components";

export const FullSizeContainer = styled.div`
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
`;

export const RegisterComponent = styled.div`
  font-family: "Montserrat", sans-serif;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
`;

export const RegisterForm = styled.div`
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 80%;
  min-height: 0%;
  background: #240e28;
  color: #d8247c;
  border-radius: 33px;
  opacity: 0%;
  transform: scaleY(0%);
  padding: 1em;
`;

export const RegisterFormBackBtn = styled.button`
  font-family: "Montserrat", sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 1em;
  background: #240e28;
  color: #d8247c;
  position: absolute;
  top: 1em;
  left: 1em;
  width: 3em;
  height: 3em;
  margin: 0;
  padding: 0;
  border-radius: 0.3em;
  border: none;
`;

export const RegisterFormContentWrapper = styled.div`
  opacity: 0;
  height: 100%;
  width: 90%;
  margin: 0;
  padding: 0;
`;

export const RegisterFormMainTitle = styled.h1`
  padding: 0;
  margin: 0;
  font-style: normal;
  font-weight: bold;
  font-size: 3em;
  color: ${(props) => props.color || "#d8247c"};
`;

export const RegisterFormFieldWrapper = styled.div`
  width: 95%;
  padding: 0.1em;
`;

export const RegisterFormFieldTitle = styled.h2`
  font-style: normal;
  font-weight: 500;
  font-size: 1.3em;
`;

export const RegisterFormFieldTitleAnnotation = styled.span`
  color: #521a4a;
`;

export const RegisterFormFieldInput = styled.input`
  background: #521a4a;
  border-radius: 13px;
  border: none;
  padding: 0.1em;
  padding-left: 20px;
  width: 99%;
  box-sizing: border-box;
  height: 2.5em;
  color: #240e28;
  font-family: "Montserrat", sans-serif;
  font-weight: 500;
  font-size: 1.2em;
`;

export const RegisterFormSubmitBtnWrapper = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 1em;
  margin-bottom: 1em;
`;

export const RegisterFormSubmitBtn = styled.button`
  margin: 0.5em;
  min-height: 2em;
  width: 55%;
  background: #d8247c;
  border-radius: 10px;
  font-family: Montserrat;
  font-style: normal;
  font-weight: 600;
  font-size: 1.5em;
  color: #240e28;
  border: none;

  background-color: ${(props) => props.color || "#d8247c"};

  &:hover {
    background-color: #ab4599;
    transition: 0.3s;
  }

  &:active {
    background-color: ${(props) =>
      props.color == "#d8247c" || !props.color ? "#25a9f0" : "#d8247c"};
    transition: 0.05s;
  }
`;

const LoaderAnimation = keyframes`
  0% {
    left:0%;
    right:100%;
    width:0%;
  }
  10% {
    left:0%;
    right:75%;
    width:25%;
  }
  90% {
    right:0%;
    left:75%;
    width:25%;
  }
  100% {
    left:100%;
    right:0%;
    width:0%;
  }
`;

export const RegisterFormLoader = styled.div`
  opacity: 0;
  position: absolute;
  border-radius: 10px;
  top: 0;
  right: 100%;
  bottom: 0;
  left: 0;
  background: #25a9f0;
  width: 0;
  animation: ${LoaderAnimation} 2s linear infinite;
`;

export const RegisterFormNotificationWrapper = styled.div`
  position: absolute;
  transform: scale(0%);
  opacity: 0%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 90%;
  padding: 1em;
`;

export const HomeContainer = styled.div`
  font-family: "Montserrat", sans-serif;
  width: 100%;
  height: 100%;
  display: flex;
`;

export const NavbarContainer = styled.div`
  position: fixed;
  width: 100%;
  min-height: 3em;
  background-color: #240e28;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.2em;
`;

export const NavbarContainerWrapper = styled.div`
  width: 90%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0;
  padding: 0;
`;

export const NavbarTitle = styled.h1`
  font-family: Montserrat;
  font-style: normal;
  font-weight: bold;
  font-size: 2em;
  color: #d8247c;
  margin: 0;
  padding: 0.2em;
`;

export const NavbarTitleAnnotation = styled.span`
  color: #fff;
`;

export const LinkList = styled.ul`
  list-style: none;
  margin: 0;
  padding: 0;
  width: 40%;
  display: flex;
  justify-content: right;
  align-items: center;
`;

export const LinkListElement = styled.li`
  margin: 0;
  padding: 1em;
`;

export const LinkListElementLink = styled(Link)`
  text-decoration: none;
  color: ${(props) => props.color || "#D8247C"};
  &:hover {
    color: ${(props) => (props.color == "#FFF" ? "#FFF" : "#ff81bf")};
    transition: 0.3s;
  }
`;
