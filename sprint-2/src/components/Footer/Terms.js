import { styled } from 'styled-components'

const StyledTerms = styled.div`
    text-align: right;
    padding-right: 16px;

    p {
        margin: 0px;
        padding: 4px;
    }

    @media screen and (max-width: 1023px) {
        text-align: center;
        padding-right: 16px;
    }
`

const Terms = () => {
    return (
        <StyledTerms>
            <p>© 2023 NexusBank. Todos los derechos reservados.</p>
            <p>
                Consulta nuestros
                <a href="enlace"> términos y condiciones</a>
            </p>
            <p>
                Consulta nuestra
                <a href="enlace"> política de privacidad</a>
            </p>
        </StyledTerms>
    )
}

export default Terms