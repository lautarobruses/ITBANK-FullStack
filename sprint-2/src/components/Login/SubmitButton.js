import { styled } from 'styled-components'

const StyledButton = styled.button`
    background: var(--white);
    color: var(--dark);
    font-size: 24px;
    padding: 16px 128px;
    border-radius: 32px;

    @media screen and (max-width: 1023px) {
        font-size: 24px;
        padding: 16px 96px;
        border-radius: 16px;
    }

    @media screen and (max-width: 640px) {
        font-size: 20px;
        padding: 12px 48px;
        border-radius: 16px;
    }
`

export default function SubmitButton({ id='submit' , children }){
    return (
        <StyledButton type="submit" id={id} value={id}>{ children }</StyledButton>
    )
}