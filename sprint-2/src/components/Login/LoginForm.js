import { useNavigate } from 'react-router-dom'

import { styled } from 'styled-components'

import TextBox from './TextBox'

const StyledForm = styled.form`
    background-color: var(--dark-sky-blue);
    opacity: 0.8;
    border-radius: 0 0 64px 64px;
    width: 1000px;
    height: 500px;
    margin-bottom: 32px;
    gap: 32px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    @media screen and (max-width: 1023px) {
        border-radius: 0 0 32px 32px;
        width: 600px;
    }

    @media screen and (max-width: 640px) {
        border-radius: 0 0 32px 32px;
        width: 360px;
        height: 500px;
        margin-bottom: 32px;
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

const LoginForm =() => {
    const navigate = useNavigate()

    const onSubmit = (event) => {
        event.preventDefault()
        // props.onLogin('mluukkai')
        navigate('/')
    }

    return (
        <StyledForm onSubmit={onSubmit}>
            <TextBox type='text' id='user'>Correo electronico o usuario:</TextBox>
            <div>
                <TextBox type='password' id='password'>Contraseña:</TextBox>
                <a href="coming-soon.html">Olvide mi contraseña</a>
            </div>
            <StyledButton type="submit" id="login" value="login">Iniciar sesion</StyledButton>
        </StyledForm>
    )
}

export default LoginForm