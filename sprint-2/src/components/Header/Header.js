import { styled } from 'styled-components'

import ButtonMenu from './ButtonMenu'

import path from '../../assets/nexusbanklogo3.png'

const StyledHeader = styled.header`
    position: fixed;
    background-color: var(--white);
    width: 100%;
    height: 10%;
    padding: 20px;

    display: flex;
    align-items: center;
    justify-content: center;

    @media screen and (max-width: 640px) {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
`
const StyledLogo = styled.img`
    height: 150%;
    width: auto;
`

const Header = () => {
    return (
        <StyledHeader>
            <StyledLogo src={path} alt='logo Nexus Bank' />
            <ButtonMenu />
        </StyledHeader>
    )
}

export default Header