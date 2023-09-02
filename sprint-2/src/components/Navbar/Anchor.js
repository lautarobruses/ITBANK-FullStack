import { styled } from 'styled-components'

const StyledAnchor = styled.a`
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
    }

    svg {
        margin-right: 16px;
    }
`

const Anchor = ({ svg, text, href }) => {
    return (
        <StyledAnchor href={href}>
            {svg}
            {text}
        </StyledAnchor>
    )
}

export default Anchor