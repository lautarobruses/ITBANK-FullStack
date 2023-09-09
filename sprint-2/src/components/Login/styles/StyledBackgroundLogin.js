import { styled } from 'styled-components'
import background from '../../../assets/background.jpg'

const StyledBackgroundLogin = styled.div`
    position: absolute;
    background-attachment: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url(${background});
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;


    a, p, span, label{
        font-family: 'Lato', sans-serif;
        color: var(--white);
    }
`
export default StyledBackgroundLogin