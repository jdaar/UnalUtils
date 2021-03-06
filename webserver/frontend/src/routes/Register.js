import React, { useEffect, useRef, useState } from "react";
import anime from "animejs/lib/anime.es.js";
import {
  RegisterComponent,
  RegisterForm,
  RegisterFormBackBtn,
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

  const createAccount = async () => {
    const data = {
      username: username,
      password: password,
    };
    submitAnimationRef.current.play();
    fetch("/api/user/create/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }).then(async (response) => {
      if (response.status == 201) {
        setNotification("Usuario creado exitosamente");
        document.getElementsByClassName(
          RegisterFormContentWrapper.styledComponentId
        )[0].style.position = "absolute";
        notificationAnimationRef.current.play();
      } else
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
    });
  };

  const reloadPage = () => {
    history.go(0);
  };

  const goToLogin = () => {
    history.push("/login");
  };

  const goToHome = () => {
    history.push("/");
  };

  return (
    <RegisterComponent>
      <RegisterFormBackBtn onClick={goToHome}>{"<"}</RegisterFormBackBtn>
      <RegisterForm>
        <RegisterFormContentWrapper>
          <RegisterFormMainTitle>Crear cuenta</RegisterFormMainTitle>
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
              Contrase??a
              <RegisterFormFieldTitleAnnotation>
                &nbsp;(La contrase??a de la universidad)
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
            <RegisterFormSubmitBtn onClick={createAccount}>
              Crear cuenta
            </RegisterFormSubmitBtn>
          </RegisterFormSubmitBtnWrapper>
        </RegisterFormContentWrapper>
        <RegisterFormLoader></RegisterFormLoader>
        <RegisterFormNotificationWrapper>
          <RegisterFormMainTitle color="#25A9F0">
            {notification}
          </RegisterFormMainTitle>
          <RegisterFormSubmitBtnWrapper>
            <RegisterFormSubmitBtn
              color="#25A9F0"
              onClick={(e) =>
                notification != "Usuario creado exitosamente"
                  ? reloadPage()
                  : goToLogin()
              }
            >
              {notification == "Usuario creado exitosamente"
                ? "Iniciar sesion"
                : "Volver"}
            </RegisterFormSubmitBtn>
          </RegisterFormSubmitBtnWrapper>
        </RegisterFormNotificationWrapper>
      </RegisterForm>
    </RegisterComponent>
  );
};

export default Register;
