import { styled } from 'styled-components'

const StyledBackgroundForm = styled.div `
    background-color: var(--dark-sky-blue);
    width: 1000px;
    padding: 32px;
    opacity: 0.8;
    border-radius: 0 0 64px 64px;
    margin-bottom: 32px;

    @media screen and (max-width: 1023px) {
        width: 600px;
        border-radius: 0 0 32px 32px;
    }

    @media screen and (max-width: 640px) {
        width: 360px;
        height: auto;
    }
`

export default StyledBackgroundForm