import styles from '@/styles/Footer/Contact.module.css'

import Link from 'next/link'

const Contact = () => {
    return (
        <div className={`${styles.contact}`}>
            <p>Atención al Cliente:</p>
            <Link href="/404">+54 9 11 1234-5678</Link>
            <Link href="/404">soporte@nexusbank.com</Link>
        </div>
    )
}

export default Contact