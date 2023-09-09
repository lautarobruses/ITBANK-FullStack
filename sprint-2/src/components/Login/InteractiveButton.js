import { styled } from 'styled-components'

const StyledButton = styled.button `
display: flex;
align-items: center;
justify-content: center;

background: none;
border: none;
font-size: 24px;
font-weight: normal;
color: var(--white);
cursor: pointer;
gap: 5px;
`

export default function InteractiveButton({ children }){
    return(
        <a href="login.html">
            <StyledButton id="interactive-button" type="button" value="Volver">{ children }</StyledButton>
        </a>
    )
}