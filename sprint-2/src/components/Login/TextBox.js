import { useContext } from 'react'

import { styled } from 'styled-components'

import { TypeContext } from './contexts/TypeContext'
import { IdContext } from './contexts/IdContext'

const StyledTextBoxs = styled.div`
    display: flex;
    flex-direction: column;
    gap: 16px;

    label{
        font-size: 24px;
    }

    @media screen and (max-width: 1023px) {
        label {
            font-size: 20px;
        }
    }

    @media screen and (max-width: 640px) {
        label {
            font-size: 16px;
        }
    }
`

const StyledInput = styled.input`
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    background-color: rgba(0, 0, 0, 0.25);
    border: 2px solid var(--white);
    border-radius: 16px;
    width: 655.99px;
    height: 61.5px;
    color: white;
    font-size: medium;
    padding: 16px;
    padding-right: 48px;

    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }

    @media screen and (max-width: 1023px) {
        border-radius: 16px;
        width: 500px;
        height: 60px;
    }
    
    @media screen and (max-width: 640px) {
        border-radius: 8px;
        width: 300px;
        height: 48px;
    }
`

const StyledPassword = styled.div`
    display: inline-block;
    position: relative;
    
    .button-eye {
        position: absolute;
        top: 54%;
        right: 18px;
        transform: translateY(-50%);
        border: none;
        background: none;
        cursor: pointer;
        padding: 0;
        font-size: 24px;
        color: var(--white);
    }
    
    .hide-icon {
        display: none;
    }
`

const PasswordBlock = () => {
    const type = useContext(TypeContext)
    const id = useContext(IdContext)

    return (
        <StyledPassword>
            <StyledInput type={type} id={id} name={id} required />
            <button id="toggle-password" className="button-eye" type="button" value="Ver/Ocultar">
                <svg className="show-icon"  fill="currentColor"  viewBox="0 0 16 16" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z"></path><path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"></path></svg>
                <svg className="hide-icon"  fill="currentColor" viewBox="0 0 16 16" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M13.359 11.238C15.06 9.72 16 8 16 8s-3-5.5-8-5.5a7.028 7.028 0 0 0-2.79.588l.77.771A5.944 5.944 0 0 1 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.134 13.134 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755-.165.165-.337.328-.517.486l.708.709z"></path><path d="M11.297 9.176a3.5 3.5 0 0 0-4.474-4.474l.823.823a2.5 2.5 0 0 1 2.829 2.829l.822.822zm-2.943 1.299.822.822a3.5 3.5 0 0 1-4.474-4.474l.823.823a2.5 2.5 0 0 0 2.829 2.829z"></path><path d="M3.35 5.47c-.18.16-.353.322-.518.487A13.134 13.134 0 0 0 1.172 8l.195.288c.335.48.83 1.12 1.465 1.755C4.121 11.332 5.881 12.5 8 12.5c.716 0 1.39-.133 2.02-.36l.77.772A7.029 7.029 0 0 1 8 13.5C3 13.5 0 8 0 8s.939-1.721 2.641-3.238l.708.709zm10.296 8.884-12-12 .708-.708 12 12-.708.708z"></path></svg>
            </button>
        </StyledPassword>
    )
}

const InputBlock = () => {
    const type = useContext(TypeContext)
    const id = useContext(IdContext)

    if (type === 'text' || type === 'number' || type === 'email') {
        return <StyledInput type={type} id={id} name={id} required />
    } else if (type === 'password') {
        return <PasswordBlock/>
    } else {
        return console.error('Unknown type: ' + type)
    }
}

const TextBox = ({ type = 'text', id = 'default', children }) => {
    return (
        <StyledTextBoxs>
            <label>{children}</label>
            <IdContext.Provider value={id}>
                <TypeContext.Provider value={type}>
                    <InputBlock />
                </TypeContext.Provider>
            </IdContext.Provider>
        </StyledTextBoxs>
    )
}

export default TextBox