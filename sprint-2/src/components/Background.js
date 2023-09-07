import styled, { css } from 'styled-components'

import background from '../assets/background.jpg'

const StyledDiv = styled.div`
    position: fixed;
    top: 100px;
    left: 384px;
    width: 100%;
    height: 100%;
    background-image: url(${background});
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    z-index: -1;
    
    @media screen and (max-width: 1023px) {
        left: 284px;
    }

    @media screen and (max-width: 640px) {
        top: 80px;
        left: 0%;
    }

    ${(props) => props.$isLogin && css`
        background-attachment: inherit;
        top: 0px;
        left: 0px;

        @media screen and (max-width: 1023px) {
            left: 0px;
        }
    
        @media screen and (max-width: 640px) {
            top: 0px;
            left: 0px;
        }
    `}
`

const Background = ({ login }) => {
    return <StyledDiv $isLogin={login} />
}

export default Background