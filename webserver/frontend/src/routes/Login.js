import React, { useEffect, useRef, useState } from "react";
import anime from "animejs/lib/anime.es.js";
import {
  RegisterComponent,
  RegisterForm,
  RegisterFormContentWrapper,
  RegisterFormFieldInput,
  RegisterFormFieldTitle,
  RegisterFormFieldTitleAnnotation,
  RegisterFormFieldWrapper,
  RegisterFormLoader,
  RegisterFormMainTitle,
  RegisterFormNotificationWrapper,
  RegisterFormSubmitBtn,
  RegisterFormSubmitBtnWrapper,
  RegisterFormBackBtn,
} from "../components/Styled";
import { useHistory } from "react-router-dom";

const Register = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [notification, setNotification] = useState("Crear cuenta");
  const submitAnimationRef = useRef(null);
  const notificationAnimationRef = useRef(null);
  const history = useHistory();

  useEffect(() => {
    const registerTimeline = anime.timeline({ autoplay: true });
    registerTimeline.add({
      targets: `.${RegisterForm.styledComponentId}`,
      duration: 500,
      opacity: 1,
      minHeight: "60%",
      scaleY: "100%",
      easing: "easeOutSine",
    });
    registerTimeline.add(
      {
        targets: `.${RegisterFormContentWrapper.styledComponentId}`,
        duration: 200,
        opacity: 1,
        easing: "easeInQuint",
      },
      "-=200"
    );
    const submitTimeline = anime.timeline({ autoplay: false });
    submitTimeline.add({
      targets: `.${RegisterFormContentWrapper.styledComponentId}`,
      duration: 500,
      opacity: 0,
      easing: "easeInOutQuad",
    });
    submitTimeline.add(
      {
        targets: `.${RegisterFormContentWrapper.styledComponentId}`,
        duration: 500,
        scale: ["100%", "0%"],
      },
      "-=500"
    );
    submitTimeline.add(
      {
        targets: `.${RegisterForm.styledComponentId}`,
        duration: 500,
        minHeight: "1%",
        easing: "easeInOutQuad",
      },
      "-700"
    );
    submitTimeline.add(
      {
        targets: `.${RegisterForm.styledComponentId}`,
        duration: 400,
        maxHeight: ["100%", "1%"],
        padding: [".5em", "0em"],
        easing: "easeInOutQuad",
      },
      "-=700"
    );
    submitTimeline.add({
      targets: `.${RegisterFormLoader.styledComponentId}`,
      duration: 500,
      opacity: 1,
      easing: "easeInOutQuad",
    });
    const notificationTimeline = anime.timeline({ autoplay: false });
    notificationTimeline.add({
      targets: `.${RegisterForm.styledComponentId}`,
      duration: 500,
      minHeight: ["1%", "40%"],
      backgroundColor: "#29385C",
      easing: "easeInOutQuad",
    });
    notificationTimeline.add(
      {
        targets: `.${RegisterFormLoader.styledComponentId}`,
        duration: 200,
        opacity: 0,
        easing: "easeInOutQuad",
      },
      "-=500"
    );
    notificationTimeline.add({
      targets: `.${RegisterFormNotificationWrapper.styledComponentId}`,
      duration: 200,
      scale: "100%",
      opacity: "100%",
      easing: "easeInOutQuad",
    });
    submitAnimationRef.current = submitTimeline;
    notificationAnimationRef.current = notificationTimeline;
  }, []);

  const retrieveTokens = async () => {
    const data = {
      username: username,
      password: password,
    };
    submitAnimationRef.current.play();
    fetch("/api/token/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (response.status == 200) {
          return response.json();
        } else {
          setTimeout(() => {
            setNotification("Algo ha salido mal");
            document.getElementsByClassName(
              RegisterFormContentWrapper.styledComponentId
            )[0].style.position = "absolute";
            document.getElementsByClassName(
              RegisterFormNotificationWrapper.styledComponentId
            )[0].style.position = "inherit";
            notificationAnimationRef.current.play();
          }, 4000);
        }
      })
      .then((data) => {
        if (data != undefined) {
          const setCookie = (name, value, minutes) => {
            const date = new Date();
            date.setTime(date.getTime + minutes * 60 * 1000);
            document.cookie = `${name}=${value}; path=/; expires=${date.toUTCString()};`;
          };
          setCookie("access", "", 0);
          setCookie("access", data.access, 10);
          setTimeout(() => history.push("/"), 4000);
        }
      });
  };

  const reloadPage = () => {
    history.go(0);
  };

  const goToHome = () => {
    history.push("/");
  };

  return (
    <RegisterComponent>
      <RegisterFormBackBtn onClick={goToHome}>{"<"}</RegisterFormBackBtn>
      <RegisterForm>
        <RegisterFormContentWrapper>
          <RegisterFormMainTitle>Iniciar sesion</RegisterFormMainTitle>
          <RegisterFormFieldWrapper>
            <RegisterFormFieldTitle>
              Nombre de usuario
              <RegisterFormFieldTitleAnnotation>
                &nbsp;(El nombre de usuario de la universidad)
              </RegisterFormFieldTitleAnnotation>
            </RegisterFormFieldTitle>
            <RegisterFormFieldInput
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              id="username"
            />
          </RegisterFormFieldWrapper>
          <RegisterFormFieldWrapper>
            <RegisterFormFieldTitle>
              Contraseña
              <RegisterFormFieldTitleAnnotation>
                &nbsp;(La contraseña de la universidad)
              </RegisterFormFieldTitleAnnotation>
            </RegisterFormFieldTitle>
            <RegisterFormFieldInput
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              id="password"
              type="password"
            />
          </RegisterFormFieldWrapper>
          <RegisterFormSubmitBtnWrapper>
            <RegisterFormSubmitBtn onClick={retrieveTokens}>
              Iniciar sesion
            </RegisterFormSubmitBtn>
          </RegisterFormSubmitBtnWrapper>
        </RegisterFormContentWrapper>
        <RegisterFormLoader></RegisterFormLoader>
        <RegisterFormNotificationWrapper>
          <RegisterFormMainTitle color="#25A9F0">
            {notification}
          </RegisterFormMainTitle>
          <RegisterFormSubmitBtnWrapper>
            <RegisterFormSubmitBtn color="#25A9F0" onClick={reloadPage}>
              Volver
            </RegisterFormSubmitBtn>
          </RegisterFormSubmitBtnWrapper>
        </RegisterFormNotificationWrapper>
      </RegisterForm>
    </RegisterComponent>
  );
};

export default Register;
