import React from "react";
import { RegisterComponent, RegisterForm, RegisterFormContentWrapper, RegisterFormFieldInput, RegisterFormFieldTitle, RegisterFormFieldTitleAnnotation, RegisterFormFieldWrapper, RegisterFormMainTitle, RegisterFormSubmitBtn, RegisterFormSubmitBtnWrapper } from "../components/Styled";

const CreateAccount = async () => {
	const data = {
		username: document.getElementById('username').value,
		password: document.getElementById('password').value
	}
	const response = await fetch('/api/user/create', {
		method: 'POST',
		headers: {
			'Accept': 'application/json',
      'Content-Type': 'application/json'
		}, body: JSON.stringify(data)
	})
	const responseContent = await response.json()
	console.log(responseContent)
}

const Register = () => {
	return (
		<RegisterComponent>
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
						<RegisterFormFieldInput id="username"/>
					</RegisterFormFieldWrapper>
					<RegisterFormFieldWrapper>
						<RegisterFormFieldTitle>
							Contraseña
							<RegisterFormFieldTitleAnnotation>
								&nbsp;(La contraseña de la universidad)
							</RegisterFormFieldTitleAnnotation>
						</RegisterFormFieldTitle>
						<RegisterFormFieldInput id="password" type="password"/>
					</RegisterFormFieldWrapper>
					<RegisterFormSubmitBtnWrapper>
						<RegisterFormSubmitBtn onClick={CreateAccount}>
							Crear cuenta
						</RegisterFormSubmitBtn>
					</RegisterFormSubmitBtnWrapper>
				</RegisterFormContentWrapper>
			</RegisterForm>
		</RegisterComponent>
	)
}

export default Register;