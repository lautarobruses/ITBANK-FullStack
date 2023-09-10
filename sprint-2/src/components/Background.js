import styled from 'styled-components'

import background from '../assets/background.jpg'

const StyledDiv = styled.div`
    position: fixed;
    top: 0px;
    width: 100%;
    height: 100%;
    background-image: url(${background});
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    z-index: -1;
`

const Background = () => {
    return <StyledDiv />
}

export default Background