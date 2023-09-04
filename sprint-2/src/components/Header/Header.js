import { styled } from 'styled-components'

import ButtonMenu from './ButtonMenu'

import path from '../../assets/nexusbanklogo3.png'

const StyledHeader = styled.header`
    position: fixed;
    top: 0px;
    background-color: var(--white);
    width: 100%;
    height: 100px;
    padding: 20px;

    display: flex;
    align-items: center;
    justify-content: center;

    @media screen and (max-width: 640px) {
        height: 80px;

        display: flex;
        align-items: center;
        justify-content: space-between;
    }
`
const StyledLogo = styled.img`
    height: 120%;
    width: auto;

    @media screen and (max-width: 640px) {
        height: 130%;
    }
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