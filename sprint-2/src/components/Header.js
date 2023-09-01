import logo from '../assets/nexusbanklogo3.png'

const Header = () => {
    return (
        <header>
            <img src={logo} alt='logo Nexus Bank' />
            <button id='button-menu' className='button-menu'>
                <span></span>
                <span></span>
                <span></span>
            </button>
        </header>
    )
}

export default Header