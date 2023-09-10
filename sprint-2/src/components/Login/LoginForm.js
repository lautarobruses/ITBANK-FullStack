// import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

import { styled } from 'styled-components'

import TextBox from './TextBox'

const StyledForm = styled.form`
    width: 1000px;
    height: 500px;
    
    display: flex;
    gap: 32px;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    #password-container {
        display: flex;
        gap: 12px;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
    }

    @media screen and (max-width: 1023px) {
        width: 600px;
    }

    @media screen and (max-width: 640px) {
        width: 360px;
        height: 400px;
    }
`

const StyledButton = styled.button`
    background: var(--white);
    color: var(--dark);
    font-size: 24px;
    padding: 16px 128px;
    border-radius: 32px;

    @media screen and (max-width: 1023px) {
        font-size: 24px;
        padding: 16px 96px;
        border-radius: 16px;
    }

    @media screen and (max-width: 640px) {
        font-size: 20px;
        padding: 12px 48px;
        border-radius: 16px;
    }
`

const StyledBackgroundForm = styled.div `
    background-color: var(--dark-sky-blue);
    opacity: 0.8;
    border-radius: 0 0 64px 64px;
    margin-bottom: 32px;

    @media screen and (max-width: 1023px) {
        border-radius: 0 0 32px 32px;
    }
    
    @media screen and (max-width: 640px) {
        border-radius: 0 0 32px 32px;
    }
`

const LoginForm =(props) => {
    const navigate = useNavigate()
    // const [username, setUsername] = useState('')
    // const [password, setPassword] = useState('')

    // console.log(username)
    // console.log(password)

    const handleLogin  = (event) => {
        event.preventDefault()

        const username = event.target[0].value
        const password = event.target[1].value

        const user = { username, password }

        // setUsername()
        // setPassword()

        window.localStorage.setItem(
            'loggedUser', JSON.stringify(user)
        )

        props.onLogin(username)
        navigate('/')
    }

    return (
        <StyledBackgroundForm>
            <StyledForm onSubmit={handleLogin}>
                <TextBox type='text' id='user'>Correo electronico o usuario:</TextBox>
                <div id='password-container'>
                    <TextBox type='password' id='password'>Contraseña:</TextBox>
                    <a href="coming-soon.html">Olvide mi contraseña</a>
                </div>
                <StyledButton type="submit" id="login" value="login">Iniciar sesion</StyledButton>
            </StyledForm>
        </StyledBackgroundForm>
    )
}

export default LoginForm