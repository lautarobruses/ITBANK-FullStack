import { useState } from 'react'
import styled, { css } from 'styled-components'

const StyledButtonMenu = styled.button`
    display: none;

    @media screen and (max-width: 640px) {
        background: none;
        visibility: visible;
        z-index: 200;
        width: 5rem;
        height: 5rem;
        border: none;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }
`

const StyledSpan = styled.span`
    @media screen and (max-width: 640px) {
        width: 37px;
        height: 4px;
        margin-bottom: 6px;
        position: relative;
        background: var(--dark-sky-blue);
        border-radius: 3px;
        transform-origin: 4px 0px;
        transition: all .2s linear;

        ${(props) => props.isClose && css`
            background: var(--white);  
        
            &:nth-child(1) {
                opacity: 1;
                transform: rotate(45deg) translate(0px, 0px);
                
                z-index: 101;
            }
        
            &:nth-child(2) {
                transform: rotate(-45deg) translate(-8px, 5px);
            }
        
            &:nth-child(3) {
                display: none;
            }
        `}
    }
`

const ButtonMenu = () => {
    const [isNavOpen, setIsNavOpen] = useState(false)

    const handleToggleClick = () => {
        setIsNavOpen(!isNavOpen)
    }

    return (
        <StyledButtonMenu className={isNavOpen ? 'close' : ''} onClick={handleToggleClick}>
            <StyledSpan isClose={isNavOpen} />
            <StyledSpan isClose={isNavOpen} />
            <StyledSpan isClose={isNavOpen} />
        </StyledButtonMenu>
    )
}

export default ButtonMenu