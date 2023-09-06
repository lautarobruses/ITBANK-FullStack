import TextBox from './TextBox'
import SubmitButton from './SubmitButton'
import { styled } from 'styled-components'

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

export default function LoginForm() {
    return (
        <StyledForm>
            <TextBox type='text' id='user'>Correo electronico o usuario:</TextBox>
            <div>
                <TextBox type='password' id='password'>Contraseña:</TextBox>
                <a href="coming-soon.html">Olvide mi contraseña</a>
            </div>
            <SubmitButton>Iniciar sesión</SubmitButton>
        </StyledForm>
    )
}