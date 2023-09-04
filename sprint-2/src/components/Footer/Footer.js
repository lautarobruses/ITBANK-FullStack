import { styled } from 'styled-components'

import Media from './Media'
import Contact from './Contact'
import Terms from './Terms'

const StyledFooter = styled.footer`
    position: fixed;
    top: 85%;
    background-color: var(--white);
    color: var(--dark-sky-blue);
    width: 100%;
    height: 15%;
    font-size: 16px;
    font-weight: bold;
    padding: 24px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    a {
        color: var(--dark);
        opacity: 0.5;
        text-decoration: none;
    }
    
    a:hover {
        opacity: 0.8;
    }

    @media screen and (max-width: 1023px) {
        padding: 16px;

        flex-direction: column;

        div {
            margin: 8px;
        }
    }
`

const Footer = () => {
    return (
        <StyledFooter>
            <Media />
            <Contact />
            <Terms />
        </StyledFooter>
    )
}

export default Footer