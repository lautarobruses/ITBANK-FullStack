import { Link } from 'react-router-dom'
import { styled } from 'styled-components'

const StyledFooter = styled.div`
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

const FooterLogin = () => {
    return (
        <StyledFooter>
            <div id="footer-register">
                <p>¿No tienes una cuenta? </p>
                <Link to="/login/register">¡Registrate!</Link>
            </div>
            <div id="footer-terms">
                <a href="#">Terminos</a>
                <span>|</span>
                <a href="#">Privacidad</a>
            </div>
        </StyledFooter>
    )
}

export default FooterLogin