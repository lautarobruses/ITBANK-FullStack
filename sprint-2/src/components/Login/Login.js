import HeaderForm from './HeaderForm'
import LoginForm from './LoginForm'
import { styled } from 'styled-components'
import StyledBackgroundLogin from './styles/StyledBackgroundLogin'

const StyledLogin = styled.div`

    #footer-terms, #footer-register {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 5px;
    }

    #footer-register {
        padding-top: 32px; 
    }
    #footer-terms {
        padding-top: 16px; 
    }

    #footer-terms a{
        text-decoration: none;
    }
`

export default function Login(){
    return (
        <StyledBackgroundLogin>
            <StyledLogin>
                <HeaderForm/>
                <LoginForm/>
                <div id="footer-register">
                    <p>¿No tienes una cuenta? </p>
                    <a href="#">Registrate!</a>
                </div>
                <div id="footer-terms">
                    <a href="#">Terminos</a>
                    <span>|</span>
                    <a href="#">Privacidad</a>
                </div>
            </StyledLogin>
        </StyledBackgroundLogin>
    )
}