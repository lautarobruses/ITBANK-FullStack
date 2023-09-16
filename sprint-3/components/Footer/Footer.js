import styles from '@/styles/Footer/Footer.module.css'

import Media from './Media'
import Contact from './Contact'
import Terms from './Terms'

const Footer = () => {
    return (
        <footer className={`${styles.footer}`}>
            <Media />
            <Contact />
            <Terms />
        </footer>
    )
}

export default Footer