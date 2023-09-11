import { Link } from 'react-router-dom'

import { styled } from 'styled-components'

const StyledLink = styled(Link)`
    background-color: var(--white);
    color: var(--dark-sky-blue);
    width: 100%;
    height: 48px;
    border-radius: 16px;
    padding: 12px 24px;
    text-decoration: none;
    font-size: 24px;
    font-weight: bold;

    display: flex;
    align-items: center;
    flex-direction: row;

    &:hover {
        background-color: var(--sky-blue);
        color: var(--white);
        opacity: 0.8;
    }

    &:active {
        background-color: var(--dark-sky-blue);
        color: var(--white);
        opacity: 1.0;
    }

    svg {
        margin-right: 16px;
    }
`

const NavbarLink = ({ to, svg, text }) => {
    return (
        <StyledLink to={to}>
            {svg}
            {text}
        </StyledLink>
    )
}

export default NavbarLink