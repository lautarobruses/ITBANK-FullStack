import TextBox from './TextBox'
import SubmitButton from './SubmitButton'
import { styled } from 'styled-components'
import StyledBackgroundForm from './styles/StyledBackgroundForm'

const StyledForm = styled.form`
    width: 1000px;
    height: 500px;

    gap: 32px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    @media screen and (max-width: 1023px) {
        width: 600px;
    }

    @media screen and (max-width: 640px) {
        width: 360px;
        height: 500px;
    }
`

export default function LoginForm() {
    return (
        <StyledBackgroundForm>
            <StyledForm>
                <TextBox type='text' id='user'>Correo electronico o usuario:</TextBox>
                <div>
                    <TextBox type='password' id='password'>Contraseña:</TextBox>
                    <a href="coming-soon.html">Olvide mi contraseña</a>
                </div>
                <SubmitButton id='login'>Iniciar sesión</SubmitButton>
            </StyledForm>
        </StyledBackgroundForm>
    )
}