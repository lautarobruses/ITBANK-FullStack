import { Outlet } from 'react-router-dom'

import { styled } from 'styled-components'

import HeaderForm from './HeaderForm'
import Background from '../Background'

const StyledLogin = styled.div`
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: auto;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    a, p, span, label{
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

    @media screen and (max-width: 1023px) {
        position: relative;
        margin: 64px;
    }

    @media screen and (max-width: 640px) {
        
    }
`

const Login = () => {
    return (
        <>
            <Background />
            <StyledLogin>
                <HeaderForm/>
                <Outlet/>
            </StyledLogin>
        </>
    )
}

export default Login