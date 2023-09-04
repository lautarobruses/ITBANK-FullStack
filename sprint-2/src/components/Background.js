import { styled } from 'styled-components'

import background from '../assets/background.jpg'

const StyledDiv = styled.div`
    position: fixed;
    top: 10%;
    left: 15%;
    width: 100%;
    height: 90%;
    background-image: url(${background});
    background-size: cover;
    background-position: center;
    z-index: -1;

    @media screen and (max-width: 640px) {
        left: 0%;
    }
`

const Background = () => {
    return <StyledDiv />
}

export default Background