import styles from '@/styles/Footer/Contact.module.css'

const Contact = () => {
    return (
        <ul className={`${styles.contact}`}>
            <li><p>Atención al Cliente:</p></li>
            <li><a>+54 9 11 1234-5678</a></li>
            <li><a href="mailto:soporte@nexusbank.com">soporte@nexusbank.com</a></li>
        </ul>
    )
}

export default Contact