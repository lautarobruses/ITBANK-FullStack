import Link from 'next/link'
import styles from "@/styles/NavBar.module.css";

const NavBar = () => {
    return (
        <div className={`${styles.container}`}>
            <Link href={'/'} className={`${styles.a}`}>Home</Link>
            <Link href={'/create'} className={`${styles.a}`}>Create</Link>
        </div>
    )
}

export default NavBar