import {
    Link
} from 'react-router-dom'

import { styled } from 'styled-components'

import SubmitButton from '../Login/SubmitButton'
import path from '../../assets/cable-desconectado.png'

const StyledHeader = styled.main`
    background-color: var(--white);
    border-radius: 64px;
    width: 1000px;
    height: 600px;

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
    
    gap: 20px;
    
    @media screen and (max-width: 1023px) {
        border-radius: 32px 32px 0 0;
        width: 600px;
        height: 100px;

        img {
            height: 64px;
            width: auto;
        }   
    }

    @media screen and (max-width: 640px) {
        border-radius: 32px 32px 0 0;
        width: 360px;
        height: 80px;
    
        img {
            height: 48px;
            width: auto;
        }
    }
`

export default function PageNotFound(){
    return (
        <StyledHeader>
            <h1>404</h1>
            <h2>Pagina no encontrada</h2>
            <img href={path} />
            <p>La pagina a la que intentas acceder no existe o se ha movido.</p>
            <p>Intenta volver a la pagina principal.</p>
            <Link to="/"> <SubmitButton>Ir al inicio</SubmitButton></Link>
        </StyledHeader>
    )
}