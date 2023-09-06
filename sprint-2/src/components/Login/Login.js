import HeaderForm from './HeaderForm'
import LoginForm from './LoginForm'
import { styled } from 'styled-components'
import background from '../../assets/background.jpg'

const StyledLogin = styled.div`
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url(${background});
    background-size: cover;
    background-position: center;
    z-index: -1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    a, p, span, label{
        font-family: 'Lato', sans-serif;
        color: var(--white);
    }

    #footer-terms, #footer-register {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 5px;
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
    )
}