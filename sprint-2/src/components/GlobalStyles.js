import { createGlobalStyle } from 'styled-components'

const GlobalStyles = createGlobalStyle`
    :root { /*Variables*/
        --grey: #EAEBED;
        --sky-blue: #5B8291;
        --dark-sky-blue: #2E424D;
        --dark: #252525;
        --light-sky-blue: #98DAD9;
        --white: #FFFFFF;
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box; /*De esta manera incluyo el padding y el border en la altura-ancho total*/
    }

    html {
        font-family: 'Lato', sans-serif;
        min-width: 375px;
    }
`

export default GlobalStyles