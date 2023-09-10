import { Outlet } from 'react-router-dom'
import { useEffect, useState } from 'react'

import { styled } from 'styled-components'

import HeaderForm from './HeaderForm'
import Background from '../Background'

const StyledLogin = styled.div`
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    
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
`

const Login = () => {
    const [user, setUser] = useState(null)

    console.log(user) //TODO

    useEffect(() => {
        const loggedUserJSON = window.localStorage.getItem('loggedUser')
        if (loggedUserJSON) {
            const user = JSON.parse(loggedUserJSON)
            setUser(user)
        }
    }, [])

    return (
        <>
            <Background login={true}/>
            <StyledLogin>
                <HeaderForm/>
                <Outlet/>
            </StyledLogin>
        </>
    )
}

export default Login