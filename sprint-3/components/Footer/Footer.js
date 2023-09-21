import styles from '@/styles/Footer/Footer.module.css'

import Media from './Media'
import Contact from './Contact'
import Terms from './Terms'
import ContactForm from './ContactForm'

const Footer = () => {
    return (
        <footer className={`${styles.footer}`}>
            <div className={`${styles.leftContainer}`}>
                <Media />
                <Contact />
                <Terms />
            </div>
            <ContactForm />
        </footer>
    )
}

export default Footer