import { styled } from 'styled-components'

import ButtonMenu from './ButtonMenu'

import path from '../../assets/nexusbanklogo3.png'

const StyledHeader = styled.header`
    background-color: var(--white);
    width: 100%;
    height: 100;
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
    width: 256px;
    height: auto;

    @media screen and (max-width: 640px) {
        width: 192px;
        height: auto;
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