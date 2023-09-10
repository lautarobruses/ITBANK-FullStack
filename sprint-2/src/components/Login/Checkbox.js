import { styled } from 'styled-components'

const StyledCheckbox = styled.div`
    position: relative;

    label{
        font-size: large;
        padding-left: 36px;
    }

    #checkbox {
        position: absolute;
        left: 0px;
        width: 19px;
        height: 19px;
        z-index: -1;
        opacity: 0;
    }

    .control_indicator {
        position: absolute;
        top: 0px;
        height: 20px;
        width: 20px;
        background: rgba(0, 0, 0, 0.25);
        border: 1px solid var(--white);
        border-radius: 3px;
    }

    .control_indicator:hover {
        background: var(--white);
        opacity: 3;
    }

    input:checked ~ .control_indicator {
        background: color: var(--white);
    }

    .input:disabled ~ .control_indicator {
        background: #e6e6e6;
        opacity: 5;
        pointer-events: none;
    }
    .control_indicator:after {
        box-sizing: unset;
        content: '';
        position: absolute;
        display: none;
    }
    input:checked ~ .control_indicator {
        background: var(--white);
    }
    input:checked ~ .control_indicator:after {
        display: block;
    }
    .control_indicator:after {
        left: 6px;
        top: 1.9px;
        width: 4px;
        height: 9px;
        border: solid var(--dark);
        border-width: 0 1px 1px 0;
        transform: rotate(45deg);
    }

    .control_indicator::before {
        content: '';
        position: absolute;
        width: 35px;
        height: 35px;
        margin-left: -8.5px;
        margin-top: -8.5px;
        background: white;
        border-radius: 36px;
        opacity: 0.5;
        z-index: 99999;
        transform: scale(0);
    }
   
    input + .control_indicator::before {
        animation: s-ripple 250ms ease-out;
    }
    input:checked + .control_indicator::before {
        animation-name: s-ripple-dup;
    }

    @keyframes s-ripple-dup {
       0% {
           transform: scale(0);
        }
       30% {
            transform: scale(1);
        }
        60% {
            transform: scale(1);
        }
        100% {
            opacity: 0;
            transform: scale(1);
        }
    }
`
export default function Checkbox({ children }) {
    return (
        <StyledCheckbox>
            <label className="control control-checkbox">
                {children}
                <input type="checkbox" id="checkbox"/>
                <div className="control_indicator"></div>
            </label>
        </StyledCheckbox>
    )
}