import { styled } from 'styled-components'

const StyledBackgroundForm = styled.div `
    background-color: var(--dark-sky-blue);
    opacity: 0.8;
    border-radius: 0 0 64px 64px;
    margin-bottom: 32px;

    @media screen and (max-width: 1023px) {
        border-radius: 0 0 32px 32px;
    }
    
    @media screen and (max-width: 640px) {
        border-radius: 0 0 32px 32px;
    }
`

export default StyledBackgroundForm