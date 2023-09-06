import { styled } from 'styled-components'
import path from '../../assets/nexusbanklogo3.png'

const StyledHeader = styled.div`
    background-color: var(--white);
    border-radius: 64px 64px 0 0;
    width: 1000px;
    height: 100px;

    display: flex;
    justify-content: center;
    align-items: center;
    
    img {
        height: 68px;
        width: auto;
    }
    
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

export default function HeaderForm(){
    return (
        <StyledHeader>
            <img src={path} alt="logo"/>
        </StyledHeader>
    )
}