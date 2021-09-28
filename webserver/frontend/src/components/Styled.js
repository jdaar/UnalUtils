import styled, { css } from 'styled-components'

export const Button = styled.button`
	background-color: aquamarine;
	padding: 1em;
	margin: 1em;
	color: white;
`

export const FullSizeContainer = styled.div`
	height: 100%;
	width: 100%;
`

export const RegisterComponent = styled.div`
	font-family: 'Montserrat', sans-serif;
	width: 100%;
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
`

export const RegisterForm = styled.div`
	padding: 1em;
	width: 80%;
	min-height: 60%;
	background: #292D2D;
	color: #839595;
	border-radius: 33px;
`

export const RegisterFormContentWrapper = styled.div`
	height: 100%;
	margin: 1em;
`

export const RegisterFormMainTitle = styled.h1`
	padding: 0;
	margin: 0;
	font-style: normal;
	font-weight: bold;
	font-size: 3em;
`

export const RegisterFormFieldWrapper = styled.div`
	width: 95%;
	padding: .1em;
`

export const RegisterFormFieldTitle = styled.h2`
	font-style: normal;
	font-weight: 500;
	font-size: 1.3em;
`

export const RegisterFormFieldTitleAnnotation = styled.span`
	color: #424646;
`

export const RegisterFormFieldInput = styled.input`
	background: #212424;
	border-radius: 13px;
	border: none;
	padding: .2em;
	width: 100%;
	height: 3em;
	color: #4B5151;
	font-family: 'Montserrat', sans-serif;
	font-weight: 500;
	font-size: 1.2em;
	padding-left: 20px;
`

export const RegisterFormSubmitBtnWrapper = styled.div`
	width: 100%;
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
`

export const RegisterFormSubmitBtn = styled.button`
	margin: .5em;
	margin-top: 1.2em;
	height: 2em;
	width: 55%;
	background: #424A4A;
	border-radius: 10px;
	font-family: Montserrat;
	font-style: normal;
	font-weight: 600;
	font-size: 1.5em;
	color: #212424;
	border: none;
`