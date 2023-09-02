import { styled } from 'styled-components'

const StyledContact = styled.ul`
    list-style: none;    
    text-align: left;
    
    li {
        padding: 4px;
    }

    @media screen and (max-width: 1023px) {
        text-align: center;
    }
`

const Contact = () => {
    return (
        <StyledContact>
            <li><p>Atención al Cliente:</p></li>
            <li><a>+54 9 11 1234-5678</a></li>
            <li><a href="mailto:soporte@nexusbank.com">soporte@nexusbank.com</a></li>
        </StyledContact>
    )
}

export default Contact