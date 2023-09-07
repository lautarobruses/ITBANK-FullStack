import { useNavigate } from 'react-router-dom'

import { styled } from 'styled-components'
import StyledBackgroundForm from './styles/StyledBackgroundForm'

import TextBox from './TextBox'

const StyledForm = styled.form`
    width: 1000px;
    height: 500px;
    
    display: flex;
    gap: 32px;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    @media screen and (max-width: 1023px) {
        width: 600px;
    }

    @media screen and (max-width: 640px) {
        width: 360px;
        height: 400px;
        margin-bottom: 16px;
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

        console.log(event.target.value)

        const user = null

        window.localStorage.setItem(
            'loggedUser', JSON.stringify(user)
        )
        // props.onLogin('mluukkai')
        navigate('/')
    }

    return (
        <StyledBackgroundForm>
            <StyledForm onSubmit={onSubmit}>
                <TextBox type='text' id='user'>Correo electronico o usuario:</TextBox>
                <div>
                    <TextBox type='password' id='password'>Contraseña:</TextBox>
                    <a href="coming-soon.html">Olvide mi contraseña</a>
                </div>
                <StyledButton type="submit" id="login" value="login">Iniciar sesion</StyledButton>
            </StyledForm>
        </StyledBackgroundForm>
    )
}

export default LoginForm